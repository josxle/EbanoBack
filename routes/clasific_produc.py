from flask import Blueprint, jsonify, request
from models.clasific_produc import ClasificProduc
from db import db

clasificProduc_bp = Blueprint('clasific_produc', __name__)

# GET
@clasificProduc_bp.route('/clasificprod', methods=['GET'])
def get_clasifProd():
    clasificProd = ClasificProduc.query.all()
    return jsonify([
        {
            'Codigo': i.Codigo,
            'Descripcion': i.Descripcion
        } for i in clasificProd
    ])

# POST
@clasificProduc_bp.route('/clasificprod', methods=['POST'])
def post_clasifProd():
    data = request.json
    nuevo = ClasificProduc(
        Codigo=data.get('Codigo'),
        Descripcion=data.get('Descripcion')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Clasificación creada exitosamente'}), 201

# PUT
@clasificProduc_bp.route('/clasificprod/<string:codigo>', methods=['PUT'])
def put_clasifProd(codigo):
    data = request.json
    clasif = ClasificProduc.query.get_or_404(codigo)
    
    clasif.Descripcion = data.get('Descripcion', clasif.Descripcion)
    
    db.session.commit()
    return jsonify({'message': 'Clasificación actualizada exitosamente'})

# DELETE
@clasificProduc_bp.route('/clasificprod/<string:codigo>', methods=['DELETE'])
def delete_clasifProd(codigo):
    clasif = ClasificProduc.query.get_or_404(codigo)
    db.session.delete(clasif)
    db.session.commit()
    return jsonify({'message': 'Clasificación eliminada exitosamente'})
