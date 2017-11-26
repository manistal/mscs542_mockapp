import logging
from flask import Flask, url_for, render_template, g, request, redirect, current_app

from datetime import datetime, timedelta

#from mockapp.extensions import db


def create_app():
    app = Flask(__name__)
    #app.config.from_object(config)

    from mockapp.views import bp as viewbp
    app.register_blueprint(viewbp)

    return app


