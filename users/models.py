from sqlalchemy.dialects.postgresql import JSON
import sqlalchemy as sa
from datetime import datetime

from users import db

def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class UserInfo(db.Model):
    __tablename__ = "user_info"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    register_date = db.Column(db.DateTime, default=datetime.utcnow())

    profile = db.relationship("UserProfile", uselist=False)

    as_dict = as_dict


class UserProfile(db.Model):
    __tablename__ = "user_profile"

    id = db.Column(db.Integer, db.ForeignKey("user_info.id"), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    
    as_dict = as_dict

