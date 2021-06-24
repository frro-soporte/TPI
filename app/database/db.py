from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models.models import Base, Usuario

engine = create_engine('sqlite:///tpidatabase.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

try:
    Usuario.__table__.create()
except:
    pass
