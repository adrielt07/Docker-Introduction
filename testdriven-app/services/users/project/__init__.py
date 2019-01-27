# services/users/project/__init__.py

import os, sys
from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)

# Set Configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Error check
print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    '''Checks the status of API'''
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
