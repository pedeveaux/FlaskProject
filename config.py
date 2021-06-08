class Config:
    LOGFILE = "application.log"
    LOG_ROTATION = "25 MB"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = False
    LOG_BACKTRACE = True
    LOG_LEVEL = "DEBUG"
    HOST = "0.0.0.0"
    PORT = 5050
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(DevelopmentConfig):
    TESTING = True
    WTF_CSRT_ENABLED = False


class ProductionConfig(Config):
    LOG_BACKTRACE = False
    LOG_LEVEL = "INFO"
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 5080


flaskconfig = {
    "development": DevelopmentConfig,
    "profuction": ProductionConfig,
    "default": DevelopmentConfig,
    "testing": TestConfig,
}
