from flask import Flask
from flask_migrate import Migrate

migrate = Migrate()


def init_app(app: Flask, db) -> None:
    migrate.init_app(app, db)
