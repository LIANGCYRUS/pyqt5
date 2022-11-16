import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
cursor =conn.cursor()

# 发送查看数据库指令
cursor.execute('show databases')
# 获取发送指令的结果
result = cursor.fetchall()
print(result)

