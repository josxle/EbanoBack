from flask import Blueprint, jsonify, request
from db import db
from models.clientes import Clientes
from models.tipo_cliente import TipoCliente

clientes_bp = Blueprint('clientes', __name__)

# GET 
@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Clientes.query.all()
    return jsonify([
        {
            'Numero': i.Numero,
            'RazonSocial': i.RazonSocial,
            'NumTel': i.NumTel,
            'Correo': i.Correo,
            'RFC': i.RFC,
            'DirNum': i.DirNum,
            'DirCalle': i.DirCalle,
            'DirCP': i.DirCP,
            'DirCol': i.DirCol,
            'ContNomPila': i.ContNomPila,
            'ContPrimApell': i.ContPrimApell,
            'ContSegunApell': i.ContSegunApell,
            'TipoClienteCodigo': i.TipoClienteCodigo
        } for i in clientes
    ])

# POST
@clientes_bp.route('/clientes', methods=['POST'])
def post_cliente():
    data = request.json

    # Validar existencia del tipo de cliente
    tipo = TipoCliente.query.get(data.get('TipoClienteCodigo'))
    if not tipo:
        return jsonify({'error': 'Tipo de cliente no encontrado'}), 404

    nuevo = Clientes(
        RazonSocial=data.get('RazonSocial'),
        NumTel=data.get('NumTel'),
        Correo=data.get('Correo'),
        RFC=data.get('RFC'),
        DirNum=data.get('DirNum'),
        DirCalle=data.get('DirCalle'),
        DirCP=data.get('DirCP'),
        DirCol=data.get('DirCol'),
        ContNomPila=data.get('ContNomPila'),
        ContPrimApell=data.get('ContPrimApell'),
        ContSegunApell=data.get('ContSegunApell'),
        TipoClienteCodigo=data.get('TipoClienteCodigo')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Cliente creado exitosamente'}), 201

# PUT
@clientes_bp.route('/clientes/<int:numero>', methods=['PUT'])
def put_cliente(numero):
    data = request.json
    cliente = Clientes.query.get_or_404(numero)

    cliente.RazonSocial = data.get('RazonSocial', cliente.RazonSocial)
    cliente.NumTel = data.get('NumTel', cliente.NumTel)
    cliente.Correo = data.get('Correo', cliente.Correo)
    cliente.RFC = data.get('RFC', cliente.RFC)
    cliente.DirNum = data.get('DirNum', cliente.DirNum)
    cliente.DirCalle = data.get('DirCalle', cliente.DirCalle)
    cliente.DirCP = data.get('DirCP', cliente.DirCP)
    cliente.DirCol = data.get('DirCol', cliente.DirCol)
    cliente.ContNomPila = data.get('ContNomPila', cliente.ContNomPila)
    cliente.ContPrimApell = data.get('ContPrimApell', cliente.ContPrimApell)
    cliente.ContSegunApell = data.get('ContSegunApell', cliente.ContSegunApell)

    if 'TipoClienteCodigo' in data:
        tipo = TipoCliente.query.get(data['TipoClienteCodigo'])
        if not tipo:
            return jsonify({'error': 'Tipo de cliente no encontrado'}), 404
        cliente.TipoClienteCodigo = data['TipoClienteCodigo']

    db.session.commit()
    return jsonify({'message': 'Cliente actualizado exitosamente'})

# DELETE 
@clientes_bp.route('/clientes/<int:numero>', methods=['DELETE'])
def delete_cliente(numero):
    cliente = Clientes.query.get_or_404(numero)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado exitosamente'})
