from flask import Flask, render_template, request, redirect, url_for, flash

from .models.models import Usuario
from .forms import RegistroUsuario, Login
from .controller.users_controller import register_user, autenticacion

app = Flask(__name__, template_folder="views/templates/", static_folder="views/static/")
app.secret_key = "mysecretkey"

#modificar
@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/register/', methods = ['GET','POST'])
def register():
    try:
        register_form = RegistroUsuario(request.form)
        if request.method == 'POST':
            user_ = Usuario(username = register_form.username.data,
                            password = register_form.password.data,
                            email = register_form.email.data)
            user = register_user(user_)
            print(user.username)
            flash(f"Usuario {user.username} registrado")
            return redirect(url_for('register'))
        return render_template('register.html', form = register_form)
    except:
        return 'no registrado'

@app.route('/login/', methods = ['GET','POST'])
def login():
    try:
        login_form = Login(request.form)
        if request.method == 'POST':
            username_ = login_form.username.data
            password_ = login_form.password.data
            user_ = autenticacion(username_, password_)
            print(user_)
            if user_:
                flash(f"Logueado {user_.username}")
            return redirect(url_for('login'))
        return render_template('login.html', form = login_form)
    except:
        return 'no'

if __name__ == '__main__':
    app.run(debug=True)