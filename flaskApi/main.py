# import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request
from personsSql import *
from Sqls import personsSql
import requests

@app.route('/')
def emp():
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(personsSql.personSql)
        empRows = cursor.fetchall()
        session = requests.Session()
        print(session.cookies.get_dict())
        cursor.execute(personsSql.personColSql)
        colRows = cursor.fetchall()
        response1 = empRows
        response2 = colRows
        response = jsonify({'response1':response1,'response2':response2})
        response.headers["Access-Control-Allow-Origin"] = 'http://127.0.0.1:8001'
        response.headers['Access-Control-Allow-Credentials']='true'
        response.status_code = 200
        return response
    except Exception as e:
        print(e) 

@app.route('/postPrsn',methods=['GET','POST'])
def postPrsn():
    try:
        print('inside')
        data = request.get_json()
        conn = mysql.connection
        cursor = conn.cursor()
        insertSqls = personsSql.insertSql.format(data['personId'],'"'+data['LastName']+'"','"'+data['FirstName']+'"','"'+data['Address']+'"','"'+data['City']+'"')
        cursor.execute(insertSqls)
        conn.commit()
        response = jsonify(data)
        response.headers.add("Access-contol-Allow-orgin","*")
        return response
    except Exception as e:
        print(e)
        pass    

if __name__ == "__main__":
    app.run()         