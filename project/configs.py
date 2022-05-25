import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    """Flask Config"""

    SECRET_KEY = "secretkey"
    SESSION_COOKIE_NAME = "project"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://id:pw@localhost:3306/schema?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = list

    def __init__(self):
        db_env = os.environ.get("SQLALCHEMY_DATABASE_URI")
        if db_env:
            self.SQLALCHEMY_DATABASE_URI = db_env


class DevelopmentConfig(Config):
    """Flask Config for dev"""

    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass
