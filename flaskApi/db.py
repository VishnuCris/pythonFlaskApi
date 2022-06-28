from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'information_schema'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)
# mysql.init_app(app)