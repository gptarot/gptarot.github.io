from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])
    def api():
        return jsonify({'result': 'You will be loved!'})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)