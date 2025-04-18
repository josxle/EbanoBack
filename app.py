from flask import Flask, jsonify
from config import Config
from db import db
from flask_migrate import Migrate
from flask_cors import CORS

# Routes
from routes.clasific_produc import clasificProduc_bp
from routes.productos import productos_bp
from routes.tipo_cliente import tipoCliente_bp
from routes.clientes import clientes_bp
from routes.forma_pago import formaPago_bp
from routes.vendedores import vendedores_bp
from routes.ventas import ventas_bp
from routes.ventas_produc import ventas_produc_bp
from routes.pagos import pagos_bp

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

# Blueprint
app.register_blueprint(clasificProduc_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(tipoCliente_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(formaPago_bp)
app.register_blueprint(vendedores_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(ventas_produc_bp)
app.register_blueprint(pagos_bp)

# INDEX
@app.route('/')
def index():
    return jsonify({"INDEX": "NOBODY HERE"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
