from flask import Blueprint, request, current_app
from flask_jwt_extended import create_access_token

from app.models.User import LoginDTO, RegisterDTO, User

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/login', methods=['POST'])
def login():
    login_data = LoginDTO(**request.json)
    email = login_data.email
    password = login_data.password

    # Buscar o usuário no banco de dados pelo nome de usuário
    user = current_app.db.users.find_one({'email': email})
    user = User(user['name'], user['email'], user['password'])

    if user:
        if user.check_password(password):
            access_token = create_access_token(identity=email)
            return {'token': access_token}, 200

    return {'error': 'Usuário não encontrado ou senha inválida'}, 401

@auth_controller.route('/register', methods=['POST'])
def register():
    register_data = RegisterDTO(**request.json)
    name = register_data.name
    email = register_data.email
    password = register_data.password

    # Verificar se o usuário já existe no banco de dados
    if current_app.db.users.find_one({'email': email}):
        return {'error': 'Já existe um usuário com esse email'}, 400

    user = User(name, email, password)
    user.hash_password()

    # Inserir o novo usuário no banco de dados
    current_app.db.users.insert_one({'email': user.email, 'password': user.password, 'name': user.name})
    access_token = create_access_token(identity=email)
    return {'token': access_token }, 201
