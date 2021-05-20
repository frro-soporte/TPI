from flask import Flask
from sqlalchemy.sql.sqltypes import DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate, init, upgrade, migrate
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
from sqlalchemy.sql import table, column
from config import DevConfig
from datetime import datetime
import os


# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
migrateObj = Migrate()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    migrateObj.init_app(app, db)


    with app.app_context():
        # Include our Routes
        from .home import home
        validate_database()
        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app


def validate_database():
    engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url): # Checks for the first time  
        create_database(engine.url)     # Create new DB    
        print(f"New Database {DevConfig.DATABASE_SCHEMA} Created") # Verifies if database is there or not.
    else:
        print(f"Database {DevConfig.DATABASE_SCHEMA} Already Exists")
    if not os.path.isdir('./migrations'):
        init(directory='migrations', multidb=False)
        print(f"Migrations folder created")
    migrate(directory='migrations', message=f'{datetime.now().strftime("%d_%m_%y_%H:%M:%S")}', sql=False, head='head', splice=False, branch_label=None, version_path=None, rev_id=None)
    upgrade(directory='migrations', revision='head', sql=False, tag=None)



## MODELOS
class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128))
## MODELOS