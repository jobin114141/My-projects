from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "iot.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .models import admin 
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'views.signin'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return admin.query.get(int(id))
    return app


def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        #db.create_all(app=app)          
        print('Created Database!')
