from flask import Blueprint, jsonify, request
from db import db
from models.tipo_cliente import TipoCliente

tipoCliente_bp = Blueprint('tipo_cliente', __name__)

# GET
@tipoCliente_bp.route('/tipoclient', methods=['GET'])
def get_tipoclient():
    tipoclient = TipoCliente.query.all()
    return jsonify([
        {
            'Codigo': i.Codigo,
            'Descripcion': i.Descripcion
        } for i in tipoclient
    ])

# POST
@tipoCliente_bp.route('/tipoclient', methods=['POST'])
def post_tipoclient():
    data = request.json

    nuevo = TipoCliente(
        Codigo=data.get('Codigo'),
        Descripcion=data.get('Descripcion')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Producto agegado correctamente'})

# PUT
@tipoCliente_bp.route('/tipoclient/<string:codigo>', methods=['PUT'])
def put_tipoclient(Codigo):
    data = request.json
    tipoclient = TipoCliente.query.get_or_404(Codigo)

    tipoclient.Codigo = data.get('Codigo', tipoclient.Codigo)
    tipoclient.Descripcion = data.get('Descripcion', tipoclient.Descripcion)

    db.session.commit()
    return jsonify({'message': 'Tipo cliente modificado exitosamente'})

# DELETE

@tipoCliente_bp.route('/tipoclient/<string:codigo>', methods=['DELETE'])
def delete_tipoclient(Codigo):
    tipoclient = TipoCliente.query.get_or_404(Codigo)
    db.session.delete(tipoclient)
    db.session.commit()
    return jsonify({'message': 'Tipo de cliente eliminado exitosamente'})