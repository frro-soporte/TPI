from .connection_manager import engine as connection_engine
from config import DevConfig
from . import Pais

class EntityManager():
    def seed_database():
        connection_engine.execute(f"INSERT INTO {DevConfig.DATABASE_SCHEMA}.pais (nombre) VALUES ('Argentina');")