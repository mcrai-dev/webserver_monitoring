# debug
# https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from OpenSSL import SSL

# init SQLAlchemy so we can use it in models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'thisissecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mcrai/Desktop/auth_flask2/db.sqlite3'

    db.init_app(app)
    # It means you import from the module in the same directory that the module this code is in.
    # Without the dot, it would import the from first module found in the PYTHON PATH

# ==========
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    print(app)
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
