# coding=utf-8
import unittest
import sys
import time
from HTMLTestRunner import HTMLTestRunner

reload(sys)
sys.setdefaultencoding('utf-8')
# 指定测试用例为当前文件夹下的目录
test_dir = './'
report_dir = './report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_dir + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='EUV-BS端自动化测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
