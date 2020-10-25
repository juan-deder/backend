import os

from flask import Flask
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[os.environ.get('FLASK_ENV', 'development')])

    from database.models import db
    db.init_app(app)

    from app.main import main
    app.register_blueprint(main)

    db_cli = AppGroup('db')

    @db_cli.command('init')
    def init():
        db.create_all()

    app.cli.add_command(db_cli)

    return app
