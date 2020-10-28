# 导包
import pymysql

# 创建链接
connect = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='root',
                          database='books')
# 获取游标
cursor = connect.cursor()

# 执行sql
sql = 'select * from t_book;'
cursor.execute(sql)

# 获取查询结果的总记录数
print(cursor.rowcount)
# 获取查询结果的第一条数据
print('one=', cursor.fetchone())
# 获取全部的查询结果
cursor.rownumber = 0
# print('two=', cursor.fetchone())
print('all=', cursor.fetchall())
# print(cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
connect.close()