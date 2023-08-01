from flask import Flask, jsonify, request
from flask_expects_json import expects_json
from flask_cors import CORS
from api.model import generatePrompt, openai
from api.schema import REQUEST_SCHEMA
from gevent.pywsgi import WSGIServer
import api.error_handler as error_handler
import werkzeug, time, os

class GPTFlask(Flask):
    def __init__(self, *args, **kwargs):
        super(GPTFlask, self).__init__(*args, **kwargs)
        self.set_openai_api_key(os.environ.get('OPENAI_API_KEY', None))
        self.launch_openai_session()
        CORS(self)
        
        # Register error handlers
        self.register_error_handler(werkzeug.exceptions.BadRequest, error_handler.handle_bad_request)
        self.register_error_handler(werkzeug.exceptions.InternalServerError, error_handler.handle_internal_server_error)
        self.register_error_handler(werkzeug.exceptions.TooManyRequests, error_handler.handle_too_many_requests)
        self.register_error_handler(werkzeug.exceptions.NotFound, error_handler.handle_not_found)
        
        
        # Handle requests to /api route
        @self.route('/api', methods=['POST'])
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
    
   
    
    def set_openai_api_key(self, key):
        self.OPENAI_API_KEY = key
    
    def get_openai_api_key(self):
        return self.OPENAI_API_KEY
    
    def launch_openai_session(self):
        openai.api_key = self.get_openai_api_key()
        
    def run_WSGI(self):
        if not hasattr(self, 'OPENAI_API_KEY'):
            raise Exception('OPENAI_API_KEY is not defined')
        CLOUD_PORT = os.environ.get('PORT', 5000)
        SERVER = WSGIServer(('0.0.0.0', int(CLOUD_PORT)), self)
        SERVER.serve_forever()

####### EXAMPLE USAGE ON LOCALHOST (WIHOUT GUNICORN - NOT RECOMMENDED) #######

""" 
app = GPTFlask(__name__)
if __name__ == '__main__':
    app.run()
"""