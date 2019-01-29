# services/users/project/users.py

from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    '''Checks the status of API'''
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
