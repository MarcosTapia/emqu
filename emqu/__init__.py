from flask import Flask, render_template, request, redirect, url_for, flash
# Entities
from .models.entities.User import User
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

# Models
from .models.ModelUser import ModelUser

# Entities
from .models.entities.User import User

db1 = MySQL(None)
root_pathApp = None

def create_app():
    app = Flask(__name__)

    csrf=CSRFProtect()    

    root_pathApp = app.root_path    

    db = MySQL(app)
    db1 = db
    login_manager_app = LoginManager(app)    

    csrf.init_app(app)

    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = "dev",
        MYSQL_HOST = 'localhost',
        MYSQL_USER = 'root',
        MYSQL_PASSWORD = '',
        MYSQL_DB = 'emqu'        
    )

    # Registrar blueprint
    from . import system
    app.register_blueprint(system.bp)
    from . import auth
    app.register_blueprint(auth.bp)



    @app.route('/')
    def index():
        return redirect(url_for('system.login'))

    @login_manager_app.user_loader
    def load_user(id):
        return ModelUser.get_by_id(db,id)

    @app.route('/logout')
    def logout():
        logout_user()
        return render_template('auth/login.html')      

    def status_401(error):
        return redirect(url_for('/'))

    def status_404(error):
        return "<h1>Página no encontrada</h1>", 404

    #app.register_error_handler(401,status_401)
    #app.register_error_handler(404,status_404)        



    return app


#python -m flask --app todor --debug run