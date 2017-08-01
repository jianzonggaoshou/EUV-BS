# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class EquipmentCancel(unittest.TestCase):
    def setUp(self):
        print("equipmentBuild case start"),
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
        print("equipmentBuild case end")
        sleep(10)
        self.browser.quit()

    def test_equipmentCancel(self):
        # *******************新增配电室***********************
        # 资源管理
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[1]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('台账管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 收缩箭头
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/div/a/span').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[2]/div/a/span').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[3]/div/a/span').click()

        # 选取设备item
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[4]/div/span').click()
        # 删除设备
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[2]/nav6-content/div[1]/div/div[2]/div/table/tbody/tr/td[6]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[2]/nav6-content/div[5]/div/div/div[3]/button[1]').click()
        # 选取配电室item
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/div/span').click()
        sleep(1)
        # 删除配电室
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div[2]/nav6-content/div[1]/div/div[2]/div/table/tbody/tr[4]/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()


if __name__ == "__main__":
    unittest.main()
