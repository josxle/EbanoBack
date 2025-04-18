from db import db
import datetime
from models.vendedores import Vendedores
from models.clientes import Clientes

class Ventas(db.Model):
    __tablename__ = 'VENTAS'

    Folio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    Subtotal = db.Column(db.Float, nullable=False)
    IVA = db.Column(db.Float, nullable=False)
    Total = db.Column(db.Float, nullable=False)
    CantProd = db.Column(db.Integer, nullable=True)
    Saldo = db.Column(db.Float, nullable=True)

    ClienteNumero = db.Column(db.Integer, db.ForeignKey('CLIENTES.Numero'), nullable=False)
    cliente = db.relationship('Clientes', backref='ventas')

    VendedoresNumero = db.Column(db.Integer, db.ForeignKey('VENDEDORES.Numero'), nullable=False)
    vendedores = db.relationship('Vendedores', backref='ventas')

    def __str__(self):
        return f'Folio {self.Folio} - Cliente {self.ClienteNumero} - Total ${self.Total}'