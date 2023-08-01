from gevent import monkey
monkey.patch_all()

from api.gpt_flask import GPTFlask
app = GPTFlask(__name__)

if __name__ == '__main__':
    app.run_WSGI()