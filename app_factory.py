from flask import Flask

import settings
from blueprints.usuarios.urls import init_app as route_user
from ext.bcrypt_password import bcrypt
from ext.cors import cors
from ext.db import db
from ext.migrate import migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    cors.init_app(app)

    route_user(app)
    return app
