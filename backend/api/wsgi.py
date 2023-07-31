from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from api.index import create_app, os
app = create_app()

if __name__ == '__main__':
    CLOUD_PORT = os.environ.get('PORT', 5000)
    HTTP_SERVER = WSGIServer(('0.0.0.0', int(CLOUD_PORT)), app)
    HTTP_SERVER.serve_forever()