from apps import create_app
from flask_cors import CORS


app = create_app()

if __name__ == '__main__':
    CORS(app,supports_credentials=False)
    app.run(host='0.0.0.0', port=5000)