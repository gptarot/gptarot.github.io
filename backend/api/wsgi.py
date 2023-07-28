from api.index import app, os

if __name__ == '__main__':
    port = int(os.environ.get("RAILWAY_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)