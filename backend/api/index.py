from flask import Flask, jsonify, request
from flask_expects_json import expects_json
from flask_cors import CORS
from api.model import generatePrompt, openai, os
from api.schema import REQUEST_SCHEMA
import werkzeug, time

# Create the Flask app
def create_app():
    app = Flask(__name__)
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    CORS(app)
    
    # Handle bad requests
    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_bad_request(exception):
        return jsonify({'error': 'Bad Request', 'details' : str(exception)}), 400
    
    # Handle internal server errors
    @app.errorhandler(werkzeug.exceptions.InternalServerError)
    def handle_internal_server_error(exception):
        return jsonify({'error': 'Internal Server Error', 'details' : str(exception)}), 500
    
    # Handle too many requests
    @app.errorhandler(werkzeug.exceptions.TooManyRequests)
    def handle_too_many_requests(exception):
        return jsonify({'error': 'Too Many Requests', 'details' : str(exception)}), 429
    
    # Handle not found errors
    @app.errorhandler(werkzeug.exceptions.NotFound)
    def handle_not_found(exception):
        return jsonify({'error': 'Not Found', 'details' : str(exception)}), 404
    
    # Handle requests to /api route
    @app.route('/api', methods=['POST'])
    @expects_json(REQUEST_SCHEMA)
    async def api():
        try:
            data = request.json
            if not isinstance(data, dict):
                return jsonify({'error': 'Invalid data type'}), 500
            start = time.time()
            result, model = await generatePrompt(data)
            # If all models are invalid, return 403
            if result == 403:
                return jsonify({'error': 'All models are invalid'}), 403
            # If the result is valid, return it
            return jsonify({'code': 200, 
                            'data': result, 
                            'processing_time': time.time() - start, 
                            'model_used':model}), 200

        except Exception as e:
            return jsonify({'error': 'Internal Server Error', 'details' : str(e)}), 500

    # Return the Flask app
    return app


####### EXAMPLE USAGE ON LOCALHOST (WIHOUT GUNICORN - NOT RECOMMENDED) #######

"""
app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
"""