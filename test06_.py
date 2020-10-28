# 导包
import pymysql


# 创建链接
connect = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='root',
                          database='books',
                          autocommit=True)
# 获取游标
cursor = connect.cursor()

# 执行sql
sql = 'insert into t_book(id, title, pub_date) values(5, "西游记", "1986-01-01")'
cursor.execute(sql)

print("-" * 50)

# raise Exception("程序出错啦。。。")

sql = 'update t_book set title = "东游记" where title = "西游记"'
cursor.execute(sql)
# 关闭游标
cursor.close()
# 关闭连接
connect.close()