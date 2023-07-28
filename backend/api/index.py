from flask import Flask, jsonify
from flask_cors import CORS
from api.model import generatePrompt, openai, os, time

def create_app():
    app = Flask(__name__)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    CORS(app)
    @app.route("/")
    async def home():
        return jsonify({'result': 'Cố lên đá đì à'})
    @app.route('/api', methods=['GET'])
    async def api():
        start = time.time()
        result:str = await generatePrompt('prompt.json')
        return jsonify({'result': result, 'processing_time': time.time() - start})

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)