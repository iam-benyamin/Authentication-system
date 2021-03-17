from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from info import username, password, host, database
from utility import SecretKey

app = Flask(__name__)
app.config['SECRET_KEY'] = SecretKey
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{database}'
db = SQLAlchemy(app)


from users.routes import users
app.register_blueprint(users)

if __name__ == '__main__':
    app.run()
