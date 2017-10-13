# -*- coding: utf-8 -*-
import unittest
from pymysql import connect


class DataBaseTest(unittest.TestCase):
    """数据库删除用户和角色"""

    def setUp(self):
        print("test case1 start"),

    def tearDown(self):
        print("test1 case end")

    def testDataBaseDelete(self):
        """数据库删除用户和角色"""
        # 打开数据库连接
        conn = connect(
            host="172.16.40.240",
            port=3306,
            user="root",
            passwd="123456",
            db="yuv_test",
            charset="utf8")

        cursor = conn.cursor()

        # 清除数据库中表内容

        # 删除用户中以xuzhen开头的数据
        cursor.execute("DELETE FROM st_sa_user WHERE user_name LIKE 'test%';")
        # 删除用户中以15609101234开头的数据
        cursor.execute("DELETE FROM st_sa_user WHERE user_name LIKE '1561234%';")
        # 删除角色中以角色开头的数据
        cursor.execute("delete from st_sa_role WHERE role_name LIKE '角色%';")

        cursor.close()
        conn.commit()
        conn.close()
        print("Done")
