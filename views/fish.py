from flask import Blueprint, jsonify

fish_api = Blueprint('fish', __name__, url_prefix='/fish')

fish = [
  {
    'name': 'Redfish',
    'length': 28
  },
  {
    'name': 'catfish',
    'length': 13
  }
]

@fish_api.route('/')
def user_get_all():
    return jsonify(fish)
