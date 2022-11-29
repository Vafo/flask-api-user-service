from flask import Blueprint
from .models import UserInfo, UserProfile

main = Blueprint('main', __name__)

@main.get("/info/all")
def get_all_users():
    users = UserInfo.query.all()
    res = []
    for user in users:
        res.append(user.as_dict())

    return res, 200

@main.get("/profile/all")
def get_all_profile():
    user_profiles = UserProfile.query.all()
    res = []
    for user_profile in user_profiles:
        res.append(user_profile.as_dict())

    return res, 200

@main.get("/info/<username>")
def get_info(username):
    user = UserInfo.query.filter_by(username=username).first()
    if user is None:
            return {"error":"There is no such user"}, 400
    res = user.as_dict()
    del res["password"]
    # del res["id"]

    return res, 200

@main.get("/profile/<username>")
def get_profile(username):
    user = UserInfo.query.filter_by(username=username).first()
    if user is None:
            return {"error":"There is no such user"}, 400

    user_profile = user.profile
    if user_profile is None:
            return {"error":"There is no profile of this user yet"}, 400

    res = user_profile.as_dict()
    return res, 200


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