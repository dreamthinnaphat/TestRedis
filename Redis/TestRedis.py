import os
import redis
import json
from flask import Flask,request,jsonify

#connectRedis
app = Flask(__name__)
db=redis.StrictRedis(
        host='10.100.2.129',
        #host='node9152-advweb-14.app.ruk-com.cloud',
        port=6379,
        #port=11162,
        password='NBPgck55186',
        decode_responses=True)

#Show all Table
@app.route('/',methods=['GET']) 
def Show_alls():     
    name=db.keys() 
    name.sort()
    req = []     
    for i in name :         
        req.append(db.hgetall(i))     
    return jsonify(req)

#Show one Table
@app.route('/<Key>', methods=['GET'])
def Show_one(Key):
    name = db.hgetall(Key)  
    return jsonify(name)

#insert
@app.route('/insert', methods=['POST'])
def add_user():
    id = request.json['id']
    Name = request.json['Name']
    Nickname = request.json['Nickname']
    Key = request.json['Key']
    user = {"id":id, "Name":Name, "Nickname":Nickname}
    db.hmset(Key,user)
    return 'insert success!'

#update
@app.route('/<Key>', methods=['PUT'])
def update_user(Key):
    id = request.json['id']
    name = request.json['name']
    nickname = request.json['nickname']
    user = {"id":id, "name":name, "nickname":nickname}
    db.hmset(name,user)
    return 'Update data success!!!'

#Delete
@app.route('/<Key>', methods=['DELETE'])
def delete_user(Key):
    db.delete(Key)
    return 'Delete data success!!!'

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 

