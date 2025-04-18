from flask import Blueprint, jsonify, request
from db import db
from models.ventas import Ventas

ventas_bp = Blueprint('ventas', __name__)

# GET
@ventas_bp.route('/ventas', methods=['GET'])
def get_ventas():
    ventas = Ventas.query.all()
    return jsonify([
        {
            'Folio': i.Folio,
            'Fecha': i.Fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'Subtotal': i.Subtotal,
            'IVA': i.IVA,
            'Total': i.Total,
            'CantProd': i.CantProd,
            'Saldo': i.Saldo,
            'ClienteNumero': i.ClienteNumero,
            'VendedoresNumero': i.VendedoresNumero
        } for i in ventas
    ])

# POST
@ventas_bp.route('/ventas', methods=['POST'])
def post_venta():
    data = request.json

    nueva_venta = Ventas(
        Subtotal=data.get('Subtotal'),
        IVA=data.get('IVA'),
        Total=data.get('Total'),
        CantProd=data.get('CantProd'),
        Saldo=data.get('Saldo'),
        ClienteNumero=data.get('ClienteNumero'),
        VendedoresNumero=data.get('VendedoresNumero')
    )
    db.session.add(nueva_venta)
    db.session.commit()
    return jsonify({'message': 'Venta registrada correctamente'}), 201

# PUT 
@ventas_bp.route('/ventas/<int:folio>', methods=['PUT'])
def put_venta(folio):
    venta = Ventas.query.get_or_404(folio)
    data = request.json

    venta.Subtotal = data.get('Subtotal', venta.Subtotal)
    venta.IVA = data.get('IVA', venta.IVA)
    venta.Total = data.get('Total', venta.Total)
    venta.CantProd = data.get('CantProd', venta.CantProd)
    venta.Saldo = data.get('Saldo', venta.Saldo)
    venta.ClienteNumero = data.get('ClienteNumero', venta.ClienteNumero)
    venta.VendedoresNumero = data.get('VendedoresNumero', venta.VendedoresNumero)

    db.session.commit()
    return jsonify({'message': 'Venta actualizada correctamente'})

# DELETE 
@ventas_bp.route('/ventas/<int:folio>', methods=['DELETE'])
def delete_venta(folio):
    venta = Ventas.query.get_or_404(folio)
    db.session.delete(venta)
    db.session.commit()
    return jsonify({'message': 'Venta eliminada correctamente'})
