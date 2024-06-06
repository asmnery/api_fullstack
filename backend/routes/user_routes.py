from app import app, db
from models.user import User
from flask import jsonify, make_response, request, Blueprint
import traceback

user_routes = Blueprint('user_routes', __name__)

# criar usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    try:
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return make_response(jsonify({'mensagem': 'Nome de usuário já existe.'}), 400)
        if User.query.filter_by(email=data['email']).first():
            return make_response(jsonify({'mensagem': 'Email já existe.'}), 400)

        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])  
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'mensagem': 'Usuário criado com sucesso.'}), 201)
    except Exception as e:
        print(f"Error in criar_usuario: {e}")  
        print(traceback.format_exc())  
        return make_response(jsonify({'mensagem': 'Erro ao criar o usuário.'}), 500)
     
#listar todos usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        users = User.query.all()
        return make_response(jsonify({'usuários': [user.json() for user in users]}), 200)
    except:
        return make_response(jsonify({'mensagem:': 'Erro ao listar os usuários.'}), 500)
    
#listar usuário por id
@app.route('/usuarios/<int:id>', methods=['GET'])
def listar_usuario_id(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'usuário': user.json()}), 200)
        return make_response(jsonify({'mensagem': 'Usuário não encontrado.'}), 404)    
    except:
        return make_response(jsonify({'mensagem': 'Erro ao listar o usuário.'}))

#atualizar usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'mensagem': 'Usuário atualizado com sucesso.'}), 200)
        return make_response(jsonify({'mensagem': 'Usuário não encontrado.'}), 404)
    except:
        return make_response(jsonify({'mensagem: Erro ao atualizar o usuário.'}), 500)
    
#deletar usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'mensagem': 'Usuário deletado com sucesso.'}), 200)
        return make_response(jsonify({'mensagem': 'Usuário não encontrado.'}), 404)
    except:
        return make_response(jsonify({'mensagem: Erro ao deletar o usuário.'}), 500)