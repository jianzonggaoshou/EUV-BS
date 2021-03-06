# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login

reload(sys)
sys.setdefaultencoding('utf8')


class BSSafeBagBuild(unittest.TestCase):
    """BS端增加安全包"""
    # 变量赋值
    safe_bag = u'安全包test'
    remark = u'备注test'
    page_name = u'第一页'
    page_sequence = '1'
    content = u'安全手册注意事项123'

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        sleep(3)
        Login.user_login(self.browser)
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(10)
        self.browser.quit()

    def test9_BSSafeBagBuild(self):
        """BS端增加安全包"""
        # 安全包管理
        self.browser.find_element_by_xpath('//div[@expander-title="安全包管理"]').click()
        sleep(1)
        # 新建
        sleep(2)
        self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()
        # 表单
        # 安全包详情
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="package.securityName"]').send_keys(
            BSSafeBagBuild.safe_bag)
        sleep(1)
        self.browser.find_element_by_xpath('//textarea[@ng-model="package.securityRemark"]').send_keys(
            BSSafeBagBuild.remark)
        # 提交
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()
        # 页列表
        sleep(1)
        self.browser.find_element_by_xpath('//button[@title="页列表"]').click()
        # 新建
        sleep(1)
        self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()

        # 页名
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="page.pageName"]').send_keys(BSSafeBagBuild.page_name)

        # 页码
        sleep(1)
        self.browser.find_element_by_xpath('//input[@ng-model="page.pageSequence"]').send_keys(
            BSSafeBagBuild.page_sequence)

        sleep(1)
        self.browser.switch_to.frame('ueditor_0')
        sleep(1)
        self.browser.find_element_by_tag_name('body').send_keys(BSSafeBagBuild.content)

        # 跳出框架
        sleep(1)
        self.browser.switch_to.parent_frame()
        # 提交
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        self.browser.find_element_by_xpath('//div[@expander-title="安全包管理"]').click()
        sleep(1)
        resultSafeBag = self.browser.find_element_by_xpath('//td[@data-title-text="安全包名"]').text
        # 去除文件中含有的空格等符号
        resultSafeBag = resultSafeBag.strip()
        print(resultSafeBag),
        sleep(1)
        self.assertEqual(resultSafeBag, BSSafeBagBuild.safe_bag, msg="添加的安全包与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
