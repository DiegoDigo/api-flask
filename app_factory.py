import settings

from flask import Flask

from blueprints.usuarios.model import User
from blueprints.usuarios.rotas import init_app as route_user
from ext.bcrypt_password import bcrypt
from ext.migrate import migrate
from ext.db import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    route_user(app)
    return app
