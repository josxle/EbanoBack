from db import db

class Vendedores(db.Model):
    __tablename__ = 'VENDEDORES'

    Numero = db.Column(db.Integer, primary_key=True)
    nomPila = db.Column(db.String(30), nullable=False)
    PrimerApell = db.Column(db.String(30), nullable=False)
    SegunApell = db.Column(db.String(30), nullable=True)
    NumTel = db.Column(db.String(15), nullable=False)
    Correo = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'{self.Numero} - {self.nomPila} {self.PrimerApell}'  