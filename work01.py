# 插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
# 测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的值：250
# 老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
# 你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？
# 导包
import pymysql

# 创建连接
connect = pymysql.connect(host="localhost",
                          port=3306,
                          user="root",
                          password="root",
                          database='books',
                          autocommit=True)

# 获取游标
cursor = connect.cursor()

# 执行sql
sql = 'insert into t_book values(4,"python从入门到放弃","2020-01-01",50,0,0);'
cursor.execute(sql)
sql = 'update t_book set comment = 250 where title = "python从入门到放弃";'
cursor.execute(sql)
sql = 'delete from t_book where title = "python从入门到放弃";'
cursor.execute(sql)
sql = 'select * from t_book;'
cursor.execute(sql)
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭连接
connect.close()