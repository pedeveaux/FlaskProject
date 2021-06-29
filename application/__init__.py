from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import flaskconfig
from loguru import logger
import logging


db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()


class PrefixMiddleware(object):
    def __init__(self, app, prefix=""):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ["PATH_INFO"].startswith(self.prefix):
            environ["PATH_INFO"] = environ["PATH_INFO"][len(self.prefix) :]
            environ["SCRIPT_NAME"] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response("404", [("Content-Type", "text/plain")])
            return ["This url does not belong to the app.".encode()]


# create a custom handler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger_opt = logger.opt(depth=depth, exception=record.exc_info)

        logger_opt.log(level, record.getMessage())


def initialize_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)


def create_app(config_name):
    """
    Application factory to initialize the Flask app
    """
    app = Flask(__name__, static_url_path="/app/static")
    app.config.from_object(flaskconfig[config_name])
    initialize_extensions(app)

    # app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix=app.config["URL_PREFIX"])

    logger.start(
        app.config["LOGFILE"],
        level=app.config["LOG_LEVEL"],
        format="{time} {level} {message}",
        backtrace=app.config["LOG_BACKTRACE"],
        rotation=app.config["LOG_ROTATION"],
    )
    log_level = app.config["LOG_LEVEL"]
    if log_level == "INFO":
        logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
    else:
        logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)

    logger.info("****** Application Server Starting *******")
    return app


def register_blueprints(app):
    from application.auth.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
