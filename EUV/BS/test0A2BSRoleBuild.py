# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSRoleBuild(unittest.TestCase):
    """BS端增加角色"""
    # 变量赋值
    a = 'test'
    role = u'角色' + a

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.240:8888/sitopeuv")
        # self.browser.get("http://114.215.94.141:8060/sitopeuv")
        # self.browser.get("http://localhost:8080/sitopeuv/")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').clear()
        self.browser.find_element_by_id('userName').send_keys('biandongfeng')
        self.browser.find_element_by_id('userPwd').clear()
        self.browser.find_element_by_id('userPwd').send_keys('12345678')
        # 登录
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
        # 等待
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
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[11]/div[1]/i').click()
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
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav3-content/div[2]/div/form/div[2]/textarea').send_keys(
            u'备注test')
        # 确定
        self.browser.find_element_by_id('new-save').click()
        # 增加权限
        sleep(3)
        self.browser.find_elements_by_id("roleAuth")[8].click()
        # 点击全选按钮
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/nav3-content/div[5]/div/form/div/div[2]/input').click()
        # 确定
        sleep(1)
        self.browser.find_element_by_id('jur-save').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        result = self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav3-content/div[1]/table/tbody/tr[9]/td[1]').text
        print(result),
        sleep(1)
        self.assertEqual(result, u'角色test', msg="添加的角色名与网页上显示的角色名不同！")

if __name__ == '__main__':
    unittest.main()
