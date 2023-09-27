from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to the best pizza'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [
        {
            'id': r.id,
            'name': r.name,
            'address': r.address
        }
        for r in restaurants
    ]
    return jsonify(restaurant_list)

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    r = Restaurant.query.get(restaurant_id)
    if r:
        restaurant_data = {
            'id': r.id,
            'name': r.name,
            'address': r.address
        }
        return jsonify(restaurant_data)
    else:
        return make_response(jsonify({'error': 'Restaurant not found'}), 404)

@app.route('/restaurants/<int:restaurant_id>/pizzas', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    r = Restaurant.query.get(restaurant_id)
    if r:
        # Assuming RestaurantPizza has a foreign key to Restaurant, it may need to be deleted first.
        RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
        db.session.delete(r)
        db.session.commit()
        return jsonify({'message': 'Restaurant deleted'}), 200
    else:
        return make_response(jsonify({'error': 'Restaurant not found'}), 404)

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {
            'id': p.id,
            'name': p.name,
            'ingredients': p.ingredients
        }
        for p in pizzas
    ]
    return jsonify(pizza_list)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')

    if not (Pizza.query.get(pizza_id) and Restaurant.query.get(restaurant_id)):
        return make_response(jsonify({'errors': ['Invalid pizza_id or restaurant_id']}), 400)

    new_restaurant_pizza = RestaurantPizza(pizza_id=pizza_id, restaurant_id=restaurant_id, price=price)

    try:
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        # Get the associated pizza data
        pizza = Pizza.query.get(pizza_id)
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        return jsonify(pizza_data), 201
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'errors': ['Validation errors']}), 400)

if __name__ == '__main__':
    app.run(debug=True)
