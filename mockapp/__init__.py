import logging
from flask import Flask, url_for, render_template, g, request, redirect, current_app

from datetime import datetime, timedelta

from mockapp.extensions import db
from config import DefaultConfig


def create_app(config=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # Logging
    formatter = logging.Formatter(app.config['LOG_FORMAT'])
    logger_handle = logging.FileHandler(filename=app.config['LOG_FILENAME'])
    logger_handle.setFormatter(formatter)
    logger_handle.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(logger_handle)

    @app.before_request
    def before_request_log():
        app.logger.info(request.path)

    # Flask SQL Alchemy
    db.init_app(app)

    # Blueprints
    from mockapp.views import bp as viewbp
    app.register_blueprint(viewbp)

    return app


