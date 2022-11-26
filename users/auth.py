
from flask import request
from flask import jsonify
from flask import Blueprint

from werkzeug.security import generate_password_hash, check_password_hash

from users import db
from models import User

auth = Blueprint("auth", __name__)

@auth.post("/register")
def register():
    if request.is_json:
        user_input = request.get_json()
        username = user_input["username"] if "username" in user_input else None
        password = user_input["password"] if "password" in user_input else None

        if not (username and password):
            return {"error":"username or password fields are missed"}, 400



        user = User.query.filter_by(username=username).first()
        if user:
            return {"error":"Username is reseved, try other"}, 400

        new_user = User(username=username, password=generate_password_hash(password, "sha256"))
        
        db.session.add(new_user)
        db.session.commit()

        # If success
        #     return 201
        return {"success":"registered account"}, 201
        
    
    return {"error":"Only JSON is supported"}, 415

@auth.post("/login")
def login():
    if request.is_json:
        user_input = request.get_json()
        username = user_input["username"] if "username" in user_input else None
        password = user_input["password"] if "password" in user_input else None

        if not (username and password):
            return {"error":"username or password fields are missed"}, 400

        user = User.query.filter_by(username=username).first()
        if user is None:
            return {"error":"There is no such user"}, 400

        if check_password_hash(user.password, password):
            return {"success":"Correct password"}, 200
        else:
            return {"error":"Incorrect password"}, 400
        
    
    return {"error":"Only JSON is supported"}, 415