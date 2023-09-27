from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(120), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

    # Add a UniqueConstraint for the name
    __table_args__ = (
        UniqueConstraint('name', name='unique_name_constraint'),
    )

    def __repr__(self):
        return '<restaurant %r>' % self.name

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)

    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy=True))

    # Add a CheckConstraint for the price
    __table_args__ = (
        CheckConstraint('price BETWEEN 1 AND 30', name='check_price_range'),
    )

    def __repr__(self):
        return '<restaurant_pizza %r>' % self.price

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

    def __repr__(self):
        return '<pizza %r>' % self.name
