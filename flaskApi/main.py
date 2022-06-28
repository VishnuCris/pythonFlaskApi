# import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request


@app.route('/')
def emp():
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_CATALOG,TABLE_SCHEMA FROM TABLES")
        empRows = cursor.fetchall()
        print(empRows)
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        # cursor.close() 
        # conn.close()
        pass 

if __name__ == "__main__":
    app.run()         