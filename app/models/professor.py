from app import db

class Professor(db.Model):
    _tablename_ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacoes = db.Column(db.Text)

    turmas = db.relationship('Turma', backref='professor', lazy=True)