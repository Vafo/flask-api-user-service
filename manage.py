from flask_migrate import Migrate

from users import create_app, db

app = create_app()

# app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user-service'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from sqlalchemy.dialects import postgresql

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))