from flask import Blueprint, jsonify, request
from models.forma_pago import FormaPago
from db import db

formaPago_bp = Blueprint('forma_pago', __name__)

# GET
@formaPago_bp.route('/formapago', methods=['GET'])
def get_formapago():
    formapago = FormaPago.query.all()
    return jsonify([
        {
            'Codigo': i.Codigo,
            'Descripcion': i.Descripcion
        } for i in formapago
    ])

# POST
@formaPago_bp.route('/formapago', methods=['POST'])
def post_formapago():
    data = request.json
    nuevo = FormaPago(
        Codigo=data.get('Codigo'),
        Descripcion=data.get('Descripcion')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Forma de pago creada exitosamente'}), 201

# PUT
@formaPago_bp.route('/formapago/<string:codigo>', methods=['PUT'])
def put_formapago(codigo):
    data = request.json
    formpag = FormaPago.query.get_or_404(codigo)
    
    formpag.Descripcion = data.get('Descripcion', formpag.Descripcion)
    
    db.session.commit()
    return jsonify({'message': 'forma de pago actualizada exitosamente'})

# DELETE
@formaPago_bp.route('/formapago/<string:codigo>', methods=['DELETE'])
def delete_formapago(codigo):
    formpag = FormaPago.query.get_or_404(codigo)
    db.session.delete(formpag)
    db.session.commit()
    return jsonify({'message': 'Forma de pago eliminada exitosamente'})
