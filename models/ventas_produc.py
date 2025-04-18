from db import db
from models.ventas import Ventas
from models.productos import Productos

class VentasProd(db.Model):
    __tablename__ = 'VENTAS_PRODUC'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    VentaFolio = db.Column(db.Integer, db.ForeignKey('VENTAS.Folio'), nullable=False)
    venta = db.relationship('Ventas', backref='ventas_produc')


    ProductoCodigo = db.Column(db.String(5), db.ForeignKey('PRODUCTOS.Codigo'), nullable=False)
    producto = db.relationship('Productos', backref='ventas_produc')

    Cantidad = db.Column(db.Integer, nullable=False)
    Importe = db.Column(db.Float, nullable=False)