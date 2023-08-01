from flask import jsonify

# Handle bad requests
def handle_bad_request(exception):
    return jsonify({'error': 'Bad Request', 'details' : str(exception)}), 400

# Handle internal server errors
def handle_internal_server_error(exception):
    return jsonify({'error': 'Internal Server Error', 'details' : str(exception)}), 500

# Handle too many requests
def handle_too_many_requests(exception):
    return jsonify({'error': 'Too Many Requests', 'details' : str(exception)}), 429

# Handle not found errors
def handle_not_found(exception):
    return jsonify({'error': 'Not Found', 'details' : str(exception)}), 404