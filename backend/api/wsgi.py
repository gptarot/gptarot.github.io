from api.index import create_app
import os

app = create_app()

if __name__ == '__main__':
    cloud_port = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=int(cloud_port), debug=True)