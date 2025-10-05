from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(_name_)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Swagger(app)

    # Importa e registra as rotas
    from app.routes.professor_routes import professor_bp
    from app.routes.turma_routes import turma_bp
    from app.routes.aluno_routes import aluno_bp

    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)

    return app