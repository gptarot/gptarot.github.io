from flask import Flask, jsonify, request
from flask_cors import CORS
import werkzeug
from api.model import generatePrompt, openai, os, time
import requests


def get_available_api_key():
    api_keys = [
        os.getenv("OPENAI_API_KEY_1"),
        os.getenv("OPENAI_API_KEY_2"),
        os.getenv("OPENAI_API_KEY_3"),
    ]
    for api_key in api_keys:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.head("https://api.openai.com/v1/usage", headers=headers)

        if "x-ratelimit-remaining" in response.headers:
            ratelimit_remaining = int(response.headers["x-ratelimit-remaining"])
            if ratelimit_remaining > 0:
                return api_key

    return None

def create_app():
    app = Flask(__name__)
    """
    available_api_key = get_available_api_key()
    if available_api_key:
        openai.api_key = available_api_key
    else:
        raise Exception("No available API key")
    """
    openai.api_key = os.getenv("OPENAI_API_KEY_1")
    CORS(app)
    
    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(e):
        return 'Bad Request!', 400
    
    @app.route("/")
    async def home():
        return jsonify({'result': 'Wrong route, please use /api'})
    
    @app.route('/api', methods=['POST'])
    async def api():
        try:
            data = request.json

            if not isinstance(data, dict):
                return jsonify({'error': 'Invalid data type'})

            start = time.time()
            result = await generatePrompt(data)
            return jsonify({'data': result, 'processing_time': time.time() - start, 'code': 200})

        except Exception as e:
            return jsonify({'error': str(e)})


    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)