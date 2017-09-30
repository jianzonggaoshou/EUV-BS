# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from public import Login

reload(sys)
sys.setdefaultencoding('utf8')


class BSRoleBuild(unittest.TestCase):
    """BS端增加角色"""
    # 变量赋值
    role = u'角色test'
    remark = u'备注test'

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

    def test2_BSRoleBuild(self):
        """BS端增加角色"""
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('//div[@expander-title="系统管理"]').click()
        sleep(1)
        self.browser.find_element_by_link_text('角色权限').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增
        sleep(2)
        self.browser.find_element_by_id('buttonToAdd').click()
        # 表单
        sleep(1)
        self.browser.find_element_by_id('name').send_keys(BSRoleBuild.role)
        self.browser.find_element_by_xpath('//textarea[@ng-model="addRole.roleRemark"]').send_keys(BSRoleBuild.remark)
        # 确定
        self.browser.find_element_by_id('new-save').click()
        # 增加权限
        sleep(3)
        self.browser.find_elements_by_id("roleAuth")[4].click()
        # 点击全选按钮
        sleep(1)
        #self.browser.find_element_by_xpath(
            #'/html/body/div/index-header/div/div[2]/div[2]/nav3-content/div[5]/div/form/div/div[2]/input').click()
        self.browser.find_element_by_xpath('//*[text()="全选"]').click()
        # 确定
        sleep(1)
        self.browser.find_element_by_id('jur-save').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        result = self.browser.find_elements_by_xpath('//td[@data-title-text="角色名称"]')[4].text
        print(result),
        sleep(1)
        self.assertEqual(result, BSRoleBuild.role, msg="添加的角色名与网页上显示的角色名不同！")


if __name__ == '__main__':
    unittest.main()
