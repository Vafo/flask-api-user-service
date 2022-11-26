from flask import Blueprint

main = Blueprint('main', __name__)

# @main.get("/show_user/<id>")
# def show_user(id):
#     user = None
#     print("Request for USER " + id)
#     user = controller.load_user(id=int(id))

#     if user:
#         response = user.to_dict()
#         return response, 201

#     return {"error":f"Could not find user {int(id)}"}, 400

# Use ? to find by id / username