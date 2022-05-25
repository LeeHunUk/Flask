from flask import Flask, g, render_template
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    """ === Flask Configs === """
    from .configs import DevelopmentConfig, ProductionConfig

    if not config:
        if app.config["DEBUG"]:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()

    app.config.from_object(config)

    """ === DB Init === """
    db.init_app(app)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    """ === CSRF Init === """
    csrf.init_app(app)

    """ === Routes Init === """
    from project.routes import base_route, auth_route

    app.register_blueprint(base_route.bp)
    # app.register_blueprint(auth_route.bp)

    """ === errorhandler === """
    e = "errors"

    @app.errorhandler(404)
    def page_404(error):

        return render_template(f"{e}/page_404.html")

    return app
