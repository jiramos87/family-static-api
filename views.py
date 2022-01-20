import requests
from flask import request, abort, send_from_directory
from datastructure import Family
from app import app



import random
from flask import jsonify

jackson_family = Family('Jackson')      

@app.route("/", methods=['GET'])
def home():
    print('hello home')
    return jackson_family.get_all_members()

@app.route("/members", methods=['GET'])
def getmembers():
    if request.method == 'GET':
        return jackson_family.get_all_members()
    else:
        return {"data": None, "status": 400} 

@app.route("/member/<int:member_id>", methods=['GET'])
def getmember(member_id):
    if request.method == 'GET':
        return jackson_family.get_member(member_id)
    else:
        return {"data": None, "status": 400} 

@app.route("/member", methods=['POST'])
def addmember():
    if request.method == 'POST':
        request_body = request.get_json()
        return jackson_family.add_member(request_body)
    else:
        return {"data": None, "status": 400} 
   
@app.route("/member/<int:member_id>", methods=['DELETE'])
def deletemember(member_id):
    if request.method == 'DELETE':
        return jackson_family.delete_member(member_id)
    else:
        return {"data": None, "status": 400}  


