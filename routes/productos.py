from flask import Blueprint, jsonify, request
from models.productos import Productos
from models.clasific_produc import ClasificProduc
from db import db

productos_bp = Blueprint('productos', __name__)

# GET
@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    prod = Productos.query.all()
    return jsonify([
        {
            'Codigo': i.Codigo,
            'Nombre': i.Codigo, 
            'Descripcion': i.Codigo,
            'Stock': i.Stock,
            'PU': i.PU,
            'ClasificacionCod': i.ClasificacionCod
        } for i in prod
    ])

# POST
@productos_bp.route('/productos', methods=['POST'])
def post_producto():
    data = request.json

    # Validar que exista la clasificación
    clasificacion = ClasificProduc.query.get(data.get('ClasificacionCod'))
    if not clasificacion:
        return jsonify({'error': 'Clasificación no encontrada'}), 404

    nuevo = Productos(
        Codigo = data.get('Codigo'),
        Nombre = data.get('Nombre'),
        Descripcion = data.get('Descripcion'),
        Stock = data.get('Stock'),
        PU = data.get('PU'),
        ClasificacionCod=data.get('ClasificacionCod')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Producto creado exitosamente'}), 201

# PUT
@productos_bp.route('/productos/<string:codigo>', methods=['PUT'])
def put_producto(codigo):
    data = request.json
    producto = Productos.query.get_or_404(codigo)

    producto.Nombre = data.get('Nombre', producto.Nombre)
    producto.Descripcion = data.get('Descripcion', producto.Descripcion)
    producto.Stock = data.get('Stock', producto.Stock)
    producto.PU = data.get('PU', producto.PU)

    if 'ClasificacionCod' in data:
        clasificacion = ClasificProduc.query.get(data.get('ClasificacionCod'))
        if not clasificacion:
            return jsonify({'error': 'Clasificación no encontrada'}), 404
        producto.ClasificacionCod = data['ClasificacionCod']

    db.session.commit()
    return jsonify({'message': 'Producto actualizado exitosamente'})

# DELETE
@productos_bp.route('/productos/<string:codigo>', methods=['DELETE'])
def delete_producto(codigo):
    producto = Productos.query.get_or_404(codigo)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'message': 'Producto eliminado exitosamente'})