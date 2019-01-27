# services/users/project/__init__.py

from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)

# Set Configuration
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    '''Checks the status of API'''
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })

