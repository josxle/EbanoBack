from flask import Blueprint, request, jsonify
from db import db
from models.ventas_produc import VentasProd

ventas_produc_bp = Blueprint('ventas_produc', __name__)

# GET
@ventas_produc_bp.route('/ventasproduc', methods=['GET'])
def get_ventas_produc():
    ventas = VentasProd.query.all()
    return jsonify([
        {
            'id': i.id,
            'VentaFolio': i.VentaFolio,
            'ProductoCodigo': i.ProductoCodigo,
            'Cantidad': i.Cantidad,
            'Importe': i.Importe
        } for i in ventas
    ])

# POST
@ventas_produc_bp.route('/ventasproduc', methods=['POST'])
def post_venta_produc():
    data = request.json

    nueva_venta_produc = VentasProd(
        VentaFolio=data.get('VentaFolio'),
        ProductoCodigo=data.get('ProductoCodigo'),
        Cantidad=data.get('Cantidad'),
        Importe=data.get('Importe')
    )
    db.session.add(nueva_venta_produc)
    db.session.commit()
    return jsonify({'message': 'Producto agregado a la venta correctamente'}), 201

# PUT
@ventas_produc_bp.route('/ventasproduc/<int:id>', methods=['PUT'])
def put_venta_produc(id):
    venta_produc = VentasProd.query.get_or_404(id)
    data = request.json

    venta_produc.VentaFolio = data.get('VentaFolio', venta_produc.VentaFolio)
    venta_produc.ProductoCodigo = data.get('ProductoCodigo', venta_produc.ProductoCodigo)
    venta_produc.Cantidad = data.get('Cantidad', venta_produc.Cantidad)
    venta_produc.Importe = data.get('Importe', venta_produc.Importe)

    db.session.commit()
    return jsonify({'message': 'Registro de producto vendido actualizado correctamente'})

# DELETE
@ventas_produc_bp.route('/ventasproduc/<int:id>', methods=['DELETE'])
def delete_venta_produc(id):
    venta_produc = VentasProd.query.get_or_404(id)
    db.session.delete(venta_produc)
    db.session.commit()
    return jsonify({'message': 'Registro de producto vendido eliminado correctamente'})
