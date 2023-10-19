import logging
import os

from flask import Flask, render_template

from .config import Config
from .routes.list import list_bp
from .routes.upload import upload_bp
from .routes.view import view_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Check if the directories exist and create them if not
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    if not os.path.exists(app.config['IMAGES_FOLDER']):
        os.makedirs(app.config['IMAGES_FOLDER'])

    # Register blueprints
    app.register_blueprint(list_bp, url_prefix='/list')
    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(view_bp, url_prefix='/view')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
