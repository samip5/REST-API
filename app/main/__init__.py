import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from .config import config_by_name

db = SQLAlchemy()
ma = Marshmallow()
flask_bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    log_file = app.config.get('LOG_FILE')
    if log_file:
        handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=3)
    else:
        handler = logging.StreamHandler()
    log_level = app.config.get('LOG_LEVEL', logging.INFO)
    log_format = app.config.get('LOG_FORMAT')
    handler.setLevel(log_level)
    handler.setFormatter(log_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)

    return app
