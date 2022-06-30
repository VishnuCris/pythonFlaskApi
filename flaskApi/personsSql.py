
from app import app
personSql = 'select * from Persons'
personColSql = 'select column_name from information_schema.columns where table_schema = "{}" and table_name = "Persons"'.format(app.config['MYSQL_DB'])