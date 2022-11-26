from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='aboba',
        SQLACLHEMY_DATABASE_URI='postgresql:///user-service'
    )
    
    db.init_app(app)

    # Instances?? https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
    
    from users.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from users.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
     

