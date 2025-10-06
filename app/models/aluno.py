from app import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)