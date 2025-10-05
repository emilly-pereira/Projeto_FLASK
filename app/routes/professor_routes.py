from flask import Blueprint, jsonify, request
from app.controllers.professor_controller import *

professor_bp = Blueprint('professor', _name_)

@professor_bp.route('/professores', methods=['GET'])
def get_professores():
    """
    Lista todos os professores
    ---
    responses:
      200:
        description: Lista de professores
    """
    professores = listar_professores()
    return jsonify([p._dict_ for p in professores])

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    """
    Retorna um professor por ID
    """
    p = buscar_professor(id)
    return jsonify(p._dict_) if p else ('Professor não encontrado', 404)

@professor_bp.route('/professores', methods=['POST'])
def post_professor():
    """
    Cria um novo professor
    """
    p = criar_professor(request.json)
    return jsonify(p._dict_), 201

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def put_professor(id):
    """
    Atualiza um professor
    """
    p = atualizar_professor(id, request.json)
    return jsonify(p._dict_)

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    """
    Deleta um professor
    """
    deletar_professor(id)
    return '', 204