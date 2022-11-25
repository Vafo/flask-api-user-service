from flask import Flask
from flask import jsonify
from flask import request
from User import User
from UserPrimitive import UserPrimitive

app = Flask(__name__)


controller = UserPrimitive()

@app.post("/register")
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

@app.get("/show_user/<id>")
def show_user(id):
    user = None
    print("Request for USER " + id)
    user = controller.load_user(id=int(id))

    if user:
        response = user.to_dict()
        return response, 201

    return {"error":f"Could not find user {id}"}, 400

@app.delete("/delete_user/<id>")
def delete_user(id):
    
    success = controller.delete_user(id=int(id))

    if success:
        return {}, 204

    return {"error":f"Could not find user {id}"}, 400
