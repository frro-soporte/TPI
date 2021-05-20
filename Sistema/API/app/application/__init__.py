from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
from config import DevConfig

# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
migrate = Migrate()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    migrate.init_app(app, db)
    validate_database()

    with app.app_context():
        # Include our Routes
        from .home import home

        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app


def validate_database():
    engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url): # Checks for the first time  
        create_database(engine.url)     # Create new DB    
        print("New Database Created") # Verifies if database is there or not.
    else:
        print("Database Already Exists")