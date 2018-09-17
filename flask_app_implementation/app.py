from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_wtf.csrf import CSRFProtect

# csrf = CSRFProtect()
app =Flask(__name__)
# csrf.init_app(app)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:root@localhost/flask_app_imp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '\x10\xd7\x13T\xf2\xd9y\xc6\xb3\t\xfe\xa0l\xa3\xc0]g\xcbA\xf5\x81\x97_,XF:Y\xe1jU\xaf'
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from views import *


if __name__ =="__main__":
	app.run(debug=True)