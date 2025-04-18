from flask import Blueprint, request, jsonify
from db import db
from models.pagos import Pagos

pagos_bp = Blueprint('pagos', __name__)

# GET
@pagos_bp.route('/pagos', methods=['GET'])
def get_pagos():
    pagos = Pagos.query.all()
    return jsonify([
        {
            'Folio': i.Folio,
            'PorcCobro': i.PorcCobro,
            'pocInteres': i.pocInteres,
            'Concepto': i.Concepto,
            'Monto': i.Monto,
            'Fecha': i.Fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'Saldo': i.Saldo,
            'VentasNum': i.VentasNum,
            'FomaPagCod': i.FomaPagCod
        } for i in pagos
    ])

# POST
@pagos_bp.route('/pagos', methods=['POST'])
def post_pago():
    data = request.json

    nuevo_pago = Pagos(
        PorcCobro=data.get('PorcCobro'),
        pocInteres=data.get('pocInteres'),
        Concepto=data.get('Concepto'),
        Monto=data.get('Monto'),
        Saldo=data.get('Saldo'),
        VentasNum=data.get('VentasNum'),
        FomaPagCod=data.get('FomaPagCod')
    )
    db.session.add(nuevo_pago)
    db.session.commit()
    return jsonify({'message': 'Pago registrado correctamente'}), 201

# PUT
@pagos_bp.route('/pagos/<int:folio>', methods=['PUT'])
def put_pago(folio):
    pago = Pagos.query.get_or_404(folio)
    data = request.json

    pago.PorcCobro = data.get('PorcCobro', pago.PorcCobro)
    pago.pocInteres = data.get('pocInteres', pago.pocInteres)
    pago.Concepto = data.get('Concepto', pago.Concepto)
    pago.Monto = data.get('Monto', pago.Monto)
    pago.Saldo = data.get('Saldo', pago.Saldo)
    pago.VentasNum = data.get('VentasNum', pago.VentasNum)
    pago.FomaPagCod = data.get('FomaPagCod', pago.FomaPagCod)

    db.session.commit()
    return jsonify({'message': 'Pago actualizado correctamente'})

# DELETE
@pagos_bp.route('/pagos/<int:folio>', methods=['DELETE'])
def delete_pago(folio):
    pago = Pagos.query.get_or_404(folio)
    db.session.delete(pago)
    db.session.commit()
    return jsonify({'message': 'Pago eliminado correctamente'})
