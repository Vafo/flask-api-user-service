from flask import Blueprint
from flask import request
from werkzeug.security import generate_password_hash

from .models import UserInfo, UserProfile
from . import db

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

@main.post("/info/<username>")
def post_info(username):
    if request.is_json:
        if check_identity(username, request.headers):
            user = UserInfo.query.filter_by(username=username).first()
            user_layout = user.as_dict()
            del user_layout["register_date"]
            del user_layout["id"]

            data = request.json
            for attr in data:
                if attr not in user_layout:
                    return {"error":"Bad JSON"}, 415

                info = data[attr]
                if attr == "password":
                    info = generate_password_hash(info, method="sha256")
                if attr == "username":
                    busy_user = UserInfo.query.filter_by(username=info).first()
                    if busy_user:
                        return {"error":"Username is busy"}, 400

                setattr(user, attr, info)
            
            # db.session.delete(user.token)
            db.session.commit()
            return user.as_dict(), 200
        
        return {"error":"You can not edit this user"}, 400


    return {"error":"Only JSON is supported"}, 415


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


@main.post("/profile/<username>")
def post_profile(username):
    if request.is_json:
        if check_identity(username, request.headers):
            user = UserInfo.query.filter_by(username=username).first()
            profile = user.profile
            data = request.json

            not_present = False
            if profile is None:
                not_present = True
                profile = UserProfile()

            profile_layout = profile.as_dict()
            del profile_layout["id"]

            for attr in data:
                if attr not in profile_layout:
                    return {"error":"Bad JSON"}, 415

                info = data[attr]
                setattr(profile, attr, info)
                
            if not_present:
                profile.id = user.id
                db.session.add(profile)
            # db.session.delete(user.token)
            db.session.commit()
            return profile.as_dict(), 200
        
        return {"error":"You can not edit this user"}, 400


    return {"error":"Only JSON is supported"}, 415


def check_identity(username, headers):
    if "Token" in headers:
        token = headers["Token"]
        user = UserInfo.query.filter_by(username=username).first()
        if user and user.token:
            return True if user.token.token == token else False
    return False

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