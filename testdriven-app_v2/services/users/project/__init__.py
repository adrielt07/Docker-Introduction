# services/users/project/__init__.py

import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print("Starting app...")

# Instantiate the db
db = SQLAlchemy()

def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # Error check
    print(app.config, file=sys.stderr)

    # shell context for clask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
