from flask import Flask, jsonify, request
from flask_cors import CORS
import werkzeug, time, os
from api.model import generatePrompt, openai

def create_app():
    app = Flask(__name__)
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    CORS(app)
    
    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(e):
        return 'Bad Request!', 400
    
    @app.route("/")
    async def home():
        return jsonify({'data': 'Wrong route, please use /api'}), 404
    
    @app.route('/api', methods=['POST'])
    async def api():
        try:
            data = request.json

            if not isinstance(data, dict):
                return jsonify({'error': 'Invalid data type'}), 500

            start = time.time()
            result = await generatePrompt(data)
            return jsonify({'data': result, 'processing_time': time.time() - start}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 403

    return app


####### EXAMPLE USAGE ON LOCALHOST (WIHOUT GUNICORN - NOT RECOMMENDED) #######

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)