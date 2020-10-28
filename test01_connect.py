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
cursor.execute('select version()')
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭连接
connect.close()