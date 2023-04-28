from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_Name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app)
    
    from .index import index
    from .dashboard import dashboard
    from .auth import auth
    from .home import Main_home
  


    
    app.register_blueprint(Main_home, url_prefix='/')
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, Manage
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'index.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


def create_database(app):
    if not path.exists('website/' + DB_Name):
        db.create_all(app=app)
        print('Created Database!')


