from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)

from routes.user_routes import user_routes
from routes.product_routes import product_routes

app.register_blueprint(user_routes)
app.register_blueprint(product_routes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)