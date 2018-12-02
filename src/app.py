from flask import Flask, jsonify
from views import user_api
from views import fish_api

app = Flask(__name__)

app.register_blueprint(user_api, url_prefix='/users')
app.register_blueprint(fish_api, url_prefix='/fish')

@app.route('/')
def index():
    return jsonify({'message': 'Works!'})

if __name__ == '__main__':
    print('Server running')
    app.run(debug=True, port=8000)