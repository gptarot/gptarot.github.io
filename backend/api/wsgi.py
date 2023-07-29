from api.index import app, os
import subprocess

if __name__ == '__main__':
    port = os.getenv("PORT", default = "5000")
    app.run(host="0.0.0.0", port=port, debug=True)