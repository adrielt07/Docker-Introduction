# services/users/project/app.py

import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print("Starting app...")
# Instantiate the app
app = Flask(__name__)

# Set Configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Error check
print(app.config, file=sys.stderr)

# Instantiate the db
db = SQLAlchemy(app)
