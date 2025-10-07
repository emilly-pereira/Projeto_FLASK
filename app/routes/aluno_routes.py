from flask import Blueprint, request, jsonify
from app.controllers import aluno_controller as controller
from flasgger import swag_from

aluno_bp = Blueprint('alunos', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'summary': 'Listar todos os alunos',
    'responses': {
        200: {
            'description': 'Lista de alunos',
            'examples': {'application/json': [{'id': 1, 'nome': 'Ana Souza', 'idade': 18}]}
        }
    }
})
def listar_alunos():
    return jsonify(controller.listar_alunos())

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'summary': 'Buscar um aluno pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Aluno encontrado'},404: {'description': 'Aluno não encontrado'}}
})
def buscar_aluno(id):
    aluno = controller.buscar_aluno(id)
    return jsonify(aluno.__dict__ if aluno else {"erro": "Aluno não encontrado"})

@aluno_bp.route('/alunos', methods=['POST'])
@swag_from({
    'tags': ['Alunos'],
    'summary': 'Criar um novo aluno',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'schema': {'type': 'object','properties': {'nome': {'type': 'string'},'idade': {'type': 'integer'}}}
    }],
    'responses': {201: {'description': 'Aluno criado com sucesso'}}
})
def criar_aluno():
    data = request.json
    novo = controller.criar_aluno(data)
    return jsonify(novo.__dict__), 201

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Alunos'],
    'summary': 'Atualizar um aluno pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'},
        {'name': 'body', 'in': 'body', 'schema': {'type': 'object','properties': {'nome': {'type': 'string'},'idade': {'type': 'integer'}}}}
    ],
    'responses': {200: {'description': 'Aluno atualizado com sucesso'},404: {'description': 'Aluno não encontrado'}}
})
def atualizar_aluno(id):
    data = request.json
    aluno = controller.atualizar_aluno(id, data)
    return jsonify(aluno.__dict__ if aluno else {"erro": "Aluno não encontrado"})

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Alunos'],
    'summary': 'Excluir um aluno pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Aluno removido com sucesso'},404: {'description': 'Aluno não encontrado'}}
})
def deletar_aluno(id):
    aluno = controller.deletar_aluno(id)
    return jsonify({"mensagem": "Aluno removido com sucesso"} if aluno else {"erro": "Aluno não encontrado"})
