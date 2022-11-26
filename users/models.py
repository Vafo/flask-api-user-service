from sqlalchemy.dialects.postgresql import JSON
import sqlalchemy as sa
from datetime import datetime

from users import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    register_date = db.Column(db.DateTime, default=datetime.utcnow())

    profile = db.relationship(
        "UserProfile", back_populates="user"
    )

class UserProfile(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(100), nullable=False)

    user = db.relationship(
        "User", back_populates="UserProfile"
    )
