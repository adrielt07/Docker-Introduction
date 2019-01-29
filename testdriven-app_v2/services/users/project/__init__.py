# services/users/project/__init__.py

import os, sys
from project.app import app
from project.users import User
from flask import jsonify

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    '''Checks the status of API'''
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
