from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = 'vishnu'
app.config['MYSQL_PASSWORD'] = 'vis@@717'
app.config['MYSQL_DB'] = 'flaskApi'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)
