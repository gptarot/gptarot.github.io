from flask import Flask, jsonify, request
from flask_expects_json import expects_json
from flask_cors import CORS
from api.model import generatePrompt, openai, os, poe
from api.schema import REQUEST_SCHEMA, ERROR_SCHEMA
import werkzeug, time

# Create the Flask app
def create_app():
    app = Flask(__name__)
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    CORS(app)
    
    # Handle bad requests
    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(e):
        validation_errors = request.expects_json_errors
        error_messages = []
        for field, errors in validation_errors.items():
            for error in errors:
                error_messages.append(f"Invalid value for '{field}': {error}")
        return jsonify({'errors': error_messages}), 400
    
    # Handle requests to / route
    @app.route("/")
    async def home():
        return jsonify({'data': 'Wrong route, please use /api'}), 404
    
    # Handle requests to /api route
    @app.route('/api', methods=['POST'])
    @expects_json(REQUEST_SCHEMA, error_schema = ERROR_SCHEMA)
    async def api():
        try:
            data = request.json
            if not isinstance(data, dict):
                return jsonify({'error': 'Invalid data type'}), 500
            start = time.time()
            result = await generatePrompt(data)
            # If all models are invalid, return 403
            if result == 403:
                return jsonify({'error': 'All models are invalid'}), 403
            # If the result is valid, return it
            return jsonify({'code': 200, 'data': result, 'processing_time': time.time() - start}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app


####### EXAMPLE USAGE ON LOCALHOST (WIHOUT GUNICORN - NOT RECOMMENDED) #######

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)