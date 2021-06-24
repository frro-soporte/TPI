from ..database import user_db
from ..models.models import Usuario

def register_user(user_: Usuario) -> Usuario:
    return user_db.register_user(user_)

def autenticacion(username_: str, pass_: str) -> Usuario:
    return user_db.autenticacion(username_,pass_)

# new = Usuario(username = 'hola4',password = '111', email = 'email1111')

# create(new)

# autenticacion('qwe','1234')