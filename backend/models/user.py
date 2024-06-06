from app import db, bcrypt
import traceback

# Model usuario
class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  

    def set_password(self, password):
        try:
            self.password = bcrypt.generate_password_hash(password).decode('utf-8')  
        except Exception as e:
            print(f"Error in set_password: {e}")
            print(traceback.format_exc())

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)  

    def json(self):
        return {'id': self.id, 'usuario': self.username, 'email': self.email, 'password': self.password}