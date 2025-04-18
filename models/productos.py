from db import db
from models.clasific_produc import ClasificProduc

class Productos(db.Model):
    __tablename__ = 'PRODUCTOS'

    Codigo = db.Column(db.String(5), primary_key=True)
    Nombre = db.Column(db.String(30), unique=True, nullable=True)
    Descripcion = db.Column(db.String(60), nullable=True)
    PU = db.Column(db.Float, nullable=True)

    ClasificacionCod = db.Column(db.String(5), db.ForeignKey('CLASIFIC_PRODUC.Codigo'), nullable=False)
    clasificacion = db.relationship('ClasificProduc', backref='productos')

    def __str__(self):
        return f'{self.Codigo} - {self.Nombre}'