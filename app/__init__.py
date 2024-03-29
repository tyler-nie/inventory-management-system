# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import app_config

# database initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name]())
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from app import model

    from .items import items_blueprint
    app.register_blueprint(items_blueprint)

    return app