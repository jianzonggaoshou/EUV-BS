# coding=utf-8
import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect(
    host="172.16.40.250",
    port=3306,
    user="sito",
    passwd="tianhuzuji@91.112",
    db="yuv_test",
    charset="utf8")

cursor = conn.cursor()

# 清除数据库中表内容

# 删除用户中以xuzhen开头的数据
cursor.execute("DELETE FROM st_sa_user WHERE user_name LIKE 'test%';")
# 删除角色中以角色开头的数据
cursor.execute("delete from st_sa_role WHERE role_name LIKE '角色%';")

cursor.close()
conn.commit()
conn.close()
print "Done"