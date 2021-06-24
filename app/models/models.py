from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()


class Usuario(Base):

    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(250), unique = True)
    password = Column(String(250))
    email = Column(String(250))

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__set_password(password)
        self.email = email

    def __set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)