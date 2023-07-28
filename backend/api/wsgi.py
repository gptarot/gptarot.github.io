from api.index import app, os
import subprocess

if __name__ == '__main__':
    railway_port = subprocess.run(["echo", "$PORT"]).stdout.decode("utf-8")
    os.environ["RAILWAY_PORT"] = railway_port
    railway_port = os.getenv("RAILWAY_PORT", default = "5000")
    app.run(host="0.0.0.0", port=railway_port, debug=True)