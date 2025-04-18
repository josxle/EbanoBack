from db import db
from models.tipo_cliente import TipoCliente  # Ajusta el import según tu estructura real

class Clientes(db.Model):
    __tablename__ = 'CLIENTES'

    Numero = db.Column(db.Integer, primary_key=True)
    RazonSocial = db.Column(db.String(80), unique=True)
    NumTel = db.Column(db.String(15), nullable=False)
    Correo = db.Column(db.String(80), nullable=False)
    RFC = db.Column(db.String(15), nullable=True)
    DirNum = db.Column(db.String(15), nullable=False)
    DirCalle = db.Column(db.String(30), nullable=False)
    DirCP = db.Column(db.Integer, nullable=False)
    DirCol = db.Column(db.String(30), nullable=False)
    ContNomPila = db.Column(db.String(30), nullable=False)
    ContPrimApell = db.Column(db.String(30), nullable=False)
    ContSegunApell = db.Column(db.String(30), nullable=False)

    TipoClienteCodigo = db.Column(db.String(5), db.ForeignKey('TIPO_CLIENTE.Codigo'), nullable=False)
    tipo_cliente = db.relationship('TipoCliente', backref='clientes')

    def __str__(self):
        return f'{self.Numero} - {self.RazonSocial}'