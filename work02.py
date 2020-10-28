# 导包
import pymysql

# 建立连接
conn = pymysql.connect("localhost", 'root', 'root', 'books', autocommit=True)
# 获取游标
cursor = conn.cursor()

sql_insert = "insert into t_book(id,title,`read`,`comment`,pub_date) values(6,'小明的哥哥叫大明',50,0,'2020-01-01');"
cursor.execute(sql_insert)
cursor.execute("select * from t_book where title='小明的哥哥叫大明';")
result = cursor.fetchall()
print("小明插入的书：", result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
