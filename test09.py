from test08 import Mysql

sql = 'select * from t_book'
result = Mysql.exe_sql(sql)
print(result)