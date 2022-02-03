from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

app = Flask(__name__, instance_relative_config=True)

# Load views
from app import views

# Setting up app configuration
app.config.from_object('config')

# Initializing flask extensions
db.init_app(app)
bootstrap.init_app(app)
