from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DevConfig

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session