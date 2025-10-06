from flask import Blueprint, jsonify, request
from app.controllers.aluno_controller import *

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():

    alunos = listar_alunos()
    return jsonify([a._dict_ for a in alunos])

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):

    a = buscar_aluno(id)
    return jsonify(a._dict_) if a else ('Aluno não encontrado', 404)

@aluno_bp.route('/alunos', methods=['POST'])
def post_aluno():

    a = criar_aluno(request.json)
    return jsonify(a._dict_), 201

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def put_aluno(id):

    a = atualizar_aluno(id, request.json)
    return jsonify(a._dict_)

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):

    deletar_aluno(id)
    return '', 204