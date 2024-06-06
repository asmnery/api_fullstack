from app import db

# Model produto
class Product(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)

    def json(self):
        return {'id': self.id, 'nome': self.nome, 'preço': self.preco, 'quantidade': self.quantidade}