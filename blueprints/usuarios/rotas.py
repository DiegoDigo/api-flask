from flask import Blueprint, Flask

from blueprints.usuarios.model import User

bp = Blueprint('user', __name__)


@bp.route("/<nome>")
def index(nome: str):
    User(nome).save()
    return ""


@bp.route("/")
def all():
    return User.find_all()


def init_app(app: Flask, url_prefix='/user') -> None:
    app.register_blueprint(bp, url_prefix=url_prefix)
