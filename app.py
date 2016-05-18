from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask.ext.restful import Api
from flask_httpauth import HTTPBasicAuth

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# api
api = Api(app)

# database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# security
auth = HTTPBasicAuth()

#users
users = {
    "admin": "password",
    "ricveal": "1234"
}