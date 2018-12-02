from flask import Blueprint, jsonify

user_api = Blueprint('user', __name__, url_prefix='/user')

users = [
  {
    'name': 'Logan',
    'age': 28
  },
  {
    'name': 'Rahul',
    'age': 28
  }
]

@user_api.route('/')
def user_get_all():
    return jsonify(users)


@user_api.route('/<string:name>')
def user_by_name(name):
    for user in users:
        if user['name'].lower() == name:
          return jsonify(user)

    return jsonify({'message': 'User not found'}), 404