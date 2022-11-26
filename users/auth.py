
from flask import request
from flask import jsonify
from flask import Blueprint

from users.User import User
from users.UserPrimitive import UserPrimitive
from users import controller

auth = Blueprint("auth", __name__)

@auth.post("/register")
def register():
    if request.is_json:
        user = User().from_dict(request.get_json())
        print(user)
        print(request.get_json())
        if(controller.save_user(user)):
            response = user.to_dict()
            del response["password"]
            return response, 201

        return {"error":"Username is reseved, try other"}, 400
    
    return {"error":"Only JSON is supported"}, 415

@auth.delete("/delete_user/<id>")
def delete_user(id):
    
    success = controller.delete_user(id=int(id))

    if success:
        return {}, 204

    return {"error":f"Could not find user {id}"}, 400