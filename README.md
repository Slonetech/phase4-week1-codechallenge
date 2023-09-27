

#Best Pizza App
This is a Flask-based web application for managing restaurants, pizzas, and restaurant-pizza associations. It allows you to view, add, and delete restaurants and pizzas, as well as create associations between specific pizzas and restaurants.

##Table of Contents
Getting Started
Project Structure
Models
Routes
Seeding Data
Getting Started
Follow these steps to set up and run the Best Pizza App on your local machine:

###Prerequisites
Python (3.x recommended)
Flask
Flask-SQLAlchemy
Flask-Migrate (for database migrations)

###Installation
Clone this repository to your local machine and cd into it:
git clone https://github.com/Slonetech/phase4-week1-codechallenge.git

Create and activate a virtual environment inside your Best Pizza App directory:
virtualenv env

Install the project dependencies:

Initialize the database and apply migrations:

flask db init
flask db migrate
flask db upgrade

Seed the database with initial data (optional, see Seeding Data).

Start the Flask development server:
use python3 app.py to start the server
or
use flask run to start the server

Open your web browser and navigate to http://localhost:5000 to access the application.

##Project Structure
The project is organized as follows:

app.py: The main Flask application file.
models.py: Defines the database models (Restaurant, RestaurantPizza, Pizza).
seed.py: A script for seeding initial data into the database.
migrations/: Contains database migration scripts created by Flask-Migrate.
venv/: A virtual environment (can be created with python -m venv venv).
Other standard Flask application files (templates, static, etc.) are not shown here for simplicity.

##Models
Restaurant
Represents a restaurant that serves pizzas.
Attributes:
id: Primary key (integer).
name: Restaurant name (string, max length 50 characters, unique).
address: Restaurant address (string, max length 120 characters).
restaurant_pizzas: Relationship with associated restaurant-pizzas.

Pizza
Represents a type of pizza.
Attributes:
id: Primary key (integer).
name: Pizza name (string, max length 80 characters).
ingredients: Pizza ingredients (string, max length 120 characters).
created_at: Timestamp indicating pizza creation time (datetime).
updated_at: Timestamp indicating pizza last update time (datetime).
restaurant_pizzas: Relationship with associated restaurant-pizzas.

RestaurantPizza
Represents an association between a restaurant and a pizza, including the pizza's price at that restaurant.
Attributes:
id: Primary key (integer).
price: Price of the pizza at the restaurant (float).
pizza_id: Foreign key linking to the associated pizza (integer).
restaurant_id: Foreign key linking to the associated restaurant (integer).
pizza: Relationship with associated pizza.
restaurant: Relationship with associated restaurant.

##Routes
The application provides the following routes:

GET /restaurants
Retrieves a list of all restaurants.
Returns JSON data in the format:

GET /restaurants/:id
Retrieves information about a specific restaurant by its ID.
Returns JSON data format and status code 200 if the restaurant exists, or status code 404 if not.

DELETE /restaurants/:id
Deletes a specific restaurant by its ID, along with associated restaurant-pizzas.
Returns an empty response body with an appropriate HTTP status code.
If the restaurant is not found, it returns a JSON error with an appropriate HTTP status code.

GET /pizzas
Retrieves a list of all pizzas.
Returns JSON data  format and status code 200.

POST /restaurant_pizzas
Creates a new restaurant-pizza association.
If the association is created successfully, it returns JSON data related to the associated pizza.
If there are validation errors or the pizza or restaurant doesn't exist, it returns a JSON error with an appropriate HTTP status code.

Seeding Data
To populate the database with initial data, you can use the seed.py script provided in the project. Follow these steps:

Open a terminal in the project directory.

Activate your virtual environment (if used).

Run the seeding script:

Copy code
python seed.py
This script creates sample restaurants, pizzas, and restaurant-pizza associations and adds them to the database.

You should see a confirmation message indicating that the data has been seeded successfully.

Now, your application has initial data for testing and development purposes.

