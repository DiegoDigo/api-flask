from flask import Blueprint, Flask, request

from blueprints.usuarios import views

bp = Blueprint('user', __name__)


@bp.route("/admin")
def create_admin():
    return views.create_user_default()


@bp.route("/authentication", methods=['POST'])
def authentication():
    return views.login(request.json)


def init_app(app: Flask, url_prefix='/user') -> None:
    app.register_blueprint(bp, url_prefix=url_prefix)
