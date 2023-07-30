from api.index import create_app
import uvicorn, os

app = create_app()

if __name__ == '__main__':
    cloud_port = os.environ.get('PORT', 5000)
    uvicorn.run(app, host='0.0.0.0',port=cloud_port)