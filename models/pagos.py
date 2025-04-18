from db import db
import datetime

from models.ventas import Ventas
from models.forma_pago import FormaPago

class Pagos(db.Model):
    __tablename__ = 'PAGOS'

    Folio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PorcCobro = db.Column(db.Integer, nullable=False)
    pocInteres = db.Column(db.Integer, nullable=False)
    Concepto = db.Column(db.String(20), nullable=False)
    Monto = db.Column(db.Float, nullable=False)
    Fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    Saldo = db.Column(db.Float, nullable=False)

    VentasNum = db.Column(db.Integer, db.ForeignKey('VENTAS.Folio'), nullable=False)
    ventas = db.relationship('Ventas', backref='pagos')

    FomaPagCod = db.Column(db.String(5), db.ForeignKey('FORMA_PAGO.Codigo'), nullable=False)
    formaPago = db.relationship('FormaPago', backref='pagos')

    def __str__(self):
        return f'{self.Folio} - {self.Fecha} {self.Saldo}'  
