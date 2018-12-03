from flask import Blueprint, Flask, jsonify, request

from blueprints.usuarios.model import User

bp = Blueprint('user', __name__)


@bp.route("/admin")
def create_admin():
    try:
        if not User.find_by_email("di3g0d0ming05@gmail.com"):
            User(username='admin', email="di3g0d0ming05@gmail.com", password="123").save()
            return jsonify({"message": "create at"}), 200
        return jsonify({"message": "User already exists!"}), 409
    except Exception as ex:
        return jsonify({"message": ex}), 400


@bp.route("/authentication", methods=['POST'])
def authentication():
    user = User.find_by_email(request.json.get('email', None))
    if user and user.password_is_valid(request.json.get('password', None)):
        return jsonify({"message": "certo"}), 200
    return jsonify({"message": "user or password not exist"}), 403


def init_app(app: Flask, url_prefix='/user') -> None:
    app.register_blueprint(bp, url_prefix=url_prefix)
