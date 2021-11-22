from flask import Flask
from flask_cors import CORS
from api.client_service import cliente

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(cliente, url_prefix='/api/cliente')


@app.route('/')
def hello():
    return "API Controle de Clientes"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
