from application import init_app
from flask_cors import CORS

app = init_app()
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')