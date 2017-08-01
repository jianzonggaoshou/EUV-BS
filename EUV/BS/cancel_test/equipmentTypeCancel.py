# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class EquipmentTypeCancel(unittest.TestCase):

    def setUp(self):
        print("equipmentTypeCancel case start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://192.168.8.88:8888/sitopeuv/")
        # self.browser.get("http://192.168.8.250:8088/sitopeuv/")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').send_keys('biandongfeng')
        self.browser.find_element_by_id('userPwd').send_keys('12345678')
        # 登录
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/p[3]/input').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("equipmentTypeCancel case end")
        sleep(10)
        self.browser.quit()

    def test_equipmentTypeCancel(self):
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('设备类型管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 选择要删除的item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[2]').click()
        # 确认删除弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()


if __name__ == "__main__":
    unittest.main()
