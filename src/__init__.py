import os 

from flask import Flask 
from . import database, auth, scoreboard, index, entry

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'sqlite'),
    )
    app.config["TEMPLATES_AUTO_RELOAD"] = True


    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    # Initializers
    database.init_app(app)
    auth.init_auth(app)
    entry.init_entries(app)

    # Blueprints
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(scoreboard.blueprint)
    app.register_blueprint(index.blueprint)
    app.register_blueprint(entry.blueprint)

    return app
