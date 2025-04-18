from flask import Flask, jsonify
from config import Config
from db import db
from flask_migrate import Migrate
from flask_cors import CORS

# Routes

# Models

from models.clasific_produc import ClasificProduc
from models.clientes import Clientes
from models.forma_pago import FormaPago
from models.pagos import Pagos
from models.productos import Productos
from models.tipo_cliente import TipoCliente
from models.vendedores import Vendedores
from models.ventas_produc import VentasProd
from models.ventas import Ventas

# Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/')
def index():
    return jsonify({"INDEX": "NOBODY HERE"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)