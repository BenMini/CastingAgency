from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config import Config
from flask_cors import CORS
# from authlib.integrations.flask_client import OAuth


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
cors = CORS()
# oauth = OAuth()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    # Reset Database
    db.drop_all()
    db.create_all()
    # oauth.init_app(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # error blueprints
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # main routes blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # auth routes blueprint
    # from app.auth import bp as auth_bp
    # app.register_blueprint(auth_bp)

    return app


APP = create_app()


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
