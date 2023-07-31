from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from api.index import *
app = create_app()

if __name__ == '__main__':
    CLOUD_PORT = os.environ.get('PORT', 5000)
    SERVER = WSGIServer(('0.0.0.0', int(CLOUD_PORT)), app)
    SERVER.serve_forever()