from flask import Blueprint, jsonify, request
from db import db
from models.vendedores import Vendedores

vendedores_bp = Blueprint('vendedores', __name__)

# GET 
@vendedores_bp.route('/vendedores', methods=['GET'])
def get_vendedores():
    vendedores = Vendedores.query.all()
    return jsonify([
        {
            'Numero': i.Numero,
            'nomPila': i.nomPila,
            'PrimerApell': i.PrimerApell,
            'SegunApell': i.SegunApell,
            'NumTel': i.NumTel,
            'Correo': i.Correo
        } for i in vendedores
    ])

# POST
@vendedores_bp.route('/vendedores', methods=['POST'])
def post_vendedor():
    data = request.json

    nuevo = Vendedores(
        nomPila=data.get('nomPila'),
        PrimerApell=data.get('PrimerApell'),
        SegunApell=data.get('SegunApell'),
        NumTel=data.get('NumTel'),
        Correo=data.get('Correo')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Vendedor creado exitosamente'}), 201

# LOGIN
@vendedores_bp.route('/vendedores/login', methods=['POST'])
def login_vendedor():
    data = request.json
    nom_pila = data.get('nomPila')
    correo = data.get('Correo')

    if not nom_pila or not correo:
        return jsonify({'message': 'Faltan campos requeridos'}), 400

    vendedor = Vendedores.query.filter_by(nomPila=nom_pila, Correo=correo).first()

    if vendedor:
        return jsonify({
            'message': 'Login exitoso',
            'vendedor': {
                'Numero': vendedor.Numero,
                'nomPila': vendedor.nomPila,
                'PrimerApell': vendedor.PrimerApell,
                'SegunApell': vendedor.SegunApell,
                'NumTel': vendedor.NumTel,
                'Correo': vendedor.Correo
            }
        }), 200
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401

# PUT 
@vendedores_bp.route('/vendedores/<int:numero>', methods=['PUT'])
def put_vendedor(numero):
    vendedor = Vendedores.query.get_or_404(numero)
    data = request.json

    vendedor.nomPila = data.get('nomPila', vendedor.nomPila)
    vendedor.PrimerApell = data.get('PrimerApell', vendedor.PrimerApell)
    vendedor.SegunApell = data.get('SegunApell', vendedor.SegunApell)
    vendedor.NumTel = data.get('NumTel', vendedor.NumTel)
    vendedor.Correo = data.get('Correo', vendedor.Correo)

    db.session.commit()
    return jsonify({'message': 'Vendedor actualizado exitosamente'})

# DELETE 
@vendedores_bp.route('/vendedores/<int:numero>', methods=['DELETE'])
def delete_vendedor(numero):
    vendedor = Vendedores.query.get_or_404(numero)
    db.session.delete(vendedor)
    db.session.commit()
    return jsonify({'message': 'Vendedor eliminado exitosamente'})