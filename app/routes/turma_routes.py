from flask import Blueprint, jsonify, request
from app.controllers.turma_controller import *

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas', methods=['GET'])
def get_turmas():

    turmas = listar_turmas()
    return jsonify([t._dict_ for t in turmas])

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):

    t = buscar_turma(id)
    return jsonify(t._dict_) if t else ('Turma não encontrada', 404)

@turma_bp.route('/turmas', methods=['POST'])
def post_turma():

    t = criar_turma(request.json)
    return jsonify(t._dict_), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def put_turma(id):

    t = atualizar_turma(id, request.json)
    return jsonify(t._dict_)

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):

    deletar_turma(id)
    return '', 204