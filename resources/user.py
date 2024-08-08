from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, create_refresh_token, get_jwt_identity
from flask.views import MethodView
from passlib.hash import pbkdf2_sha256

from db import db
from blocklist import BlockList
from models import UserModel
from schemas import UserSchema

blp = Blueprint("User", "users", description="Operation on user")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with this name exist")
        
        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()
        
        return{"messsage":"user created successfully"}, 201


@blp.route("/user/<string:user_id>")
class user(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"user deleted successfully"}, 200


@blp.route("/login")
class userLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token":access_token, "refresh_token":refresh_token}, 200
        
        abort(401, message="Invalid credentials")

@blp.route("/refresh")
class refresh_token(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200

@blp.route("/logout")
class userlogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BlockList.add(jti)
        return {"message":"Successfully logged out"}, 200