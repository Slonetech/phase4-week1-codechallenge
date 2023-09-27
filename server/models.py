from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class restaurant(db.model,SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)

    restaurant_pizzas = db.relationship('restaurant_pizza', backref='restaurant', lazy=True)

    def __repr__(self):
        return '<restaurant %r>' % self.name
    

class restaurant_pizza(db.model,SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    price = db.Column(db.integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    restaurant = db.relationship('restaurant', backref='restaurant_pizzas', lazy=True)
    pizza = db.relationship('pizza', backref='restaurant_pizzas', lazy=True)


    def __repr__(self):
        return '<restaurant_pizza %r>' % self.name
    

class pizza(db.model,SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    restaurant_pizzas = db.relationship('restaurant_pizza', backref='pizza', lazy=True)

    def __repr__(self):
        return '<pizza %r>' % self.name