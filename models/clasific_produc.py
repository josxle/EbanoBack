from db import db

class ClasificProduc(db.Model):
    __tablename__ = 'CLASIFIC_PRODUC'

    Codigo = db.Column(db.String(5), primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'{self.Codigo} - {self.Descripcion}'
