from app import app, db
from models.product import Product
from flask import jsonify, make_response, request, Blueprint

product_routes = Blueprint('product_routes', __name__)

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
            produto.nome = data['nome']
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