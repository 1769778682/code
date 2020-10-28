import pymysql

# 创建链接
connect = None
cursor = None
try:
    # 创建链接
    connect = pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='root',
                              database='books',
                              autocommit=False)
    # 获取游标
    cursor = connect.cursor()
    # 执行SQL
    sql = 'insert into t_book(id,title,pub_date) values(5,"西游记","1986-01-01")'
    cursor.execute(sql)
    raise Exception('程序出错啦。。。。')

    sql = "insert into t_hero(name,gender,book_id) values('孙悟空',1,5)"

    cursor.execute(sql)
    # 提交事务
    connect.commit()

except Exception as e:
    # 回滚数据
    connect.rollback()
    # 打印异常信息
    print(e)
finally:
    if cursor:
        # 关闭游标
        cursor.close()
    # 关闭连接
    if connect:
        connect.close()


