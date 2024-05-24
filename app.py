from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import environ
import traceback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # Inicializar o Bcrypt com a aplicação Flask

# Model usuario
class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Remover unique=True para senha

    def set_password(self, password):
        try:
            self.password = bcrypt.generate_password_hash(password).decode('utf-8')  # Usar bcrypt para hashear a senha
        except Exception as e:
            print(f"Error in set_password: {e}")
            print(traceback.format_exc())

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)  # Verificar a senha

    def json(self):
        return {'id': self.id, 'usuario': self.username, 'email': self.email, 'password': self.password}

# Model produto
class Product(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)

    def json(self):
        return {'id': self.id, 'nome': self.nome, 'preço': self.preco, 'quantidade': self.quantidade}

db.create_all()

# Rota de teste
@app.route('/teste', methods=['GET'])
def test():
    return make_response(jsonify({'mensagem': 'Teste de rota'}), 200)

# Criar usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    try:
        data = request.get_json()

        # Verificar se o username ou email já existem
        if User.query.filter_by(username=data['username']).first():
            return make_response(jsonify({'mensagem': 'Nome de usuário já existe.'}), 400)
        if User.query.filter_by(email=data['email']).first():
            return make_response(jsonify({'mensagem': 'Email já existe.'}), 400)

        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])  # Usar set_password para hashear a senha
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'mensagem': 'Usuário criado com sucesso.'}), 201)
    except Exception as e:
        print(f"Error in criar_usuario: {e}")  # Adicionar print para log de erro
        print(traceback.format_exc())  # Adicionar rastreamento de pilha
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

#criar produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    try:
        data = request.get_json()
        new_product = Product(nome=data['nome'], preco=data['preço'], quantidade=data['quantidade'])
        db.session.add(new_product)
        db.session.commit()
        return make_response(jsonify({'mensagem': 'Produto registrado com sucesso.'}), 201)
    except:
        return make_response(jsonify({' mensagem': 'Erro ao criar o produto.'}), 500)

#listar todos produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        produtos = Product.query.all()
        return make_response(jsonify({'produtos': [produto.json() for produto in produtos]}), 200)
    except:
        return make_response(jsonify({'mensagem:': 'Erro ao listar os produtos.'}), 500)

#listar produto por id
@app.route('/produtos/<int:id>', methods=['GET'])
def listar_produto_id(id):
    try:
        produto = Product.query.filter_by(id=id).first()
        if produto:
            return make_response(jsonify({'Produto': produto.json()}), 200)
        return make_response(jsonify({'mensagem': 'Produto não encontrado.'}), 404)    
    except:
        return make_response(jsonify({'mensagem': 'Erro ao listar o produto.'}))

#atualizar produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    try:
        produto = Product.query.filter_by(id=id).first()
        if produto:
            data = request.get_json()
            produto.nome = data['']
            produto.preco = data['preço']
            produto.quantidade = data['quantidade']
            db.session.commit()
            return make_response(jsonify({'mensagem': 'Produto atualizado com sucesso.'}), 200)
        return make_response(jsonify({'mensagem': 'Produto não encontrado.'}), 404)
    except:
        return make_response(jsonify({'mensagem: Erro ao atualizar o produto.'}), 500)

#deletar produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        produto = Product.query.filter_by(id=id).first()
        if produto:
            db.session.delete(produto)
            db.session.commit()
            return make_response(jsonify({'mensagem': 'Produto excluído com sucesso.'}), 200)
        return make_response(jsonify({'mensagem': 'Produto não encontrado.'}), 404)
    except:
        return make_response(jsonify({'mensagem: Erro ao excluir o produto.'}), 500)