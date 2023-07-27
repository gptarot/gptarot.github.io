from flask import Flask, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    @app.route("/")
    def home():
        return jsonify({'result': ''})
    @app.route('/api', methods=['GET'])
    def api():
        return jsonify({'result': 'Tarot Reader API'})

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)