from . import db

class Ususarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255))

    def __repr__(self):
        return '%s' % self.nome