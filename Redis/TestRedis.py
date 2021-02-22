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

#แสดงข้อมูลที่มีทั้งหมดของตาราง
@app.route('/',methods=['GET']) 
def Show_fruits():     
    name=db.keys() 
    name.sort()
    req = []     
    for i in name :         
        req.append(db.hgetall(i))     
    return jsonify(req)

#แสดงข้อมูล1อย่างในตาราง
@app.route('/<Key>', methods=['GET'])
def Show_fruit(Key):
    name = db.hgetall(Key)  
    #print (name)
    return jsonify(name)

#ใส่ข้อมูลเพิ่มในตาราง
@app.route('/insert', methods=['POST'])
def add_fruit():
    id = request.json['id']
    Name = request.json['Name']
    Nickname = request.json['Nickname']
    Key = request.json['Key']
    #print (id)
    #print (name)
    #print (price)
    user = {"id":id, "Name":Name, "Nickname":Nickname}
    db.hmset(Key,user)
    return 'insert success!'

#อัพเดทข้อมูลในตาราง
@app.route('/<Key>', methods=['PUT'])
def update_fruit(Key):
    id = request.json['id']
    name = request.json['name']
    price = request.json['price']
    print (id)
    print (name)
    print (price)
    user = {"id":id, "name":name, "price":price}
    db.hmset(name,user)
    return 'Update data success!!!'

#ลบข้อมูล
@app.route('/<Key>', methods=['DELETE'])
def delete_staff(Key):
    db.delete(Key)
    return 'Delete data success!!!'

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 

