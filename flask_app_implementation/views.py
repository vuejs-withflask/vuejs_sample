from flask import Flask, render_template, request, redirect, url_for ,jsonify, make_response,current_app
from app import app
from models import *
from flask import Response
import uuid
from werkzeug.security import generate_password_hash
import jwt
import time
from datetime import timedelta, datetime
from functools import wraps
from functools import update_wrapper
from app import db
import jwt
from flask import current_app

@app.route('/')
def root():
	return "login page"


def token_required(f):  
    @wraps(f)
    def decorated(*args,**kwargs):
        print("requets json:",request.headers)
        token = None
        if 'X-access-token' in request.headers:
            token = request.headers['X-access-token'].strip()
        if not token:
            return jsonify({'message':"token missing"}),401
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            print("print out the data :",data)
        except:
            return jsonify({"message":"token session is expired"}),401
        return f(*args,**kwargs)
    return decorated



@app.route('/registration',methods=['GET','POST'])
def index():
    print("request:{0} --------request method:{1}".format(request,request.method))
    print(request.json)
    if request.method=='POST':
        try:
            print("-"*20)
            print(request)
            u= User.query.filter_by(username=request.json["username"]).first()
            print("user:",u)
            if u:
                return Response('{"message":"username is already taken"}',status=500)
            else:
                new_user = User(request.json['username'],request.json['password'])
                db.session.add(new_user)
                db.session.commit() 
                return Response('{"message":"user creation is succesfull"}',status=200)
        except Exception as e:
            return jsonify({"error":e})

@app.route("/listusers",methods=["GET"])
@token_required
def listusers():
    l_users=[]
    u = User.query.all()
    for user in u:
        d= {"username":user.username,"password":user.password}
        l_users.append(d)
    print(l_users)
    return jsonify (l_users)


@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    user = User.authenticate(**data)
    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401
    token = jwt.encode({
        'sub': user.username,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=10)},
        current_app.config['SECRET_KEY'])
    print("token:",token)
    return jsonify({ 'token': token.decode('UTF-8') }),200

@app.route("/register", methods=['POST'])
def register():  
    data = request.get_json()
    print("----------------------------",data)
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"messge":"user is created successfully"}), 201