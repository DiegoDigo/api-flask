from flask import Blueprint, Flask, jsonify

from blueprints.usuarios.model import User

bp = Blueprint('user', __name__)


@bp.route("/<nome>")
def index(nome: str):
    User(username=nome, email="teste@gmail.com", password="123").save()
    return ""


@bp.route("/")
def all():
    pass #json(User.find_all())


def init_app(app: Flask, url_prefix='/user') -> None:
    app.register_blueprint(bp, url_prefix=url_prefix)
