import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
# Session Management
login_manager = LoginManager()
login_manager.login_view='authentication.do_the_login'
login_manager.session_protection='strong'
bcrypt = Bcrypt()


def create_app(config_type):
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # /Users/sabbha/Desktop/udemy/flask/book_catalog/config/dev.py
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main  # importing blueprint
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
