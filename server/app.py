from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, restaurant, restaurant_pizza, pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'welcome to best pizza'


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = restaurant.query.all()
    return jsonify(restaurants)


@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = restaurant.query.get(restaurant_id)
    return jsonify(restaurant)


@app.route('/restaurants/<int:restaurant_id>/pizzas', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = restaurant.query.get(restaurant_id)
    db.session.delete(restaurant)
    db.session.commit()
    return make_response(jsonify({'message': 'restaurant deleted'}), 200)


@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        for pizza in pizzas
    ]
    return jsonify(pizza_list)



@app.route('/restaurants_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')

    if not Pizza.query.get(pizza_id) or not restaurant_id:
        return make_response(jsonify({'errors': ['Invalid pizza_id or restaurant_id']}), 400)
