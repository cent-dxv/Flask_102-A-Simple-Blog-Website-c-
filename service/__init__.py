from flask import Flask 
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
db_name ='flask_102.db'
def create_app():
    app = Flask(__name__) 

    app.config['SQL_ALCHEMY_DATABASE_URL'] = f'sqlite:///{db_name}'
    db.__init__(app)
    from .auth import auth
    from .view import view



    app.register_blueprint(auth , url_prefix='/')
    app.register_blueprint(view, url_prefix='/')

    from .model import User

    create_db(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app


def create_db(app):
    if not path.exists("service/" + db_name):
        db.create_all(app=app)
        print("bd created")



