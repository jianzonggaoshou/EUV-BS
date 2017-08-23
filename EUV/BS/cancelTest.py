# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep

class CancelTest(unittest.TestCase):

    def setUp(self):
        print("test case start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.5:8888/sitopeuv")
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
        print("test case end")
        sleep(10)
        self.browser.quit()

    # @unittest.skip("直接跳过测试test1_userCancel")
    def test1_userCancel(self):
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('用户管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 删除第一个item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]/button[2]').click()
        # 确认弹窗
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test2_roleCancel")
    def test2_roleCancel(self):
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
        # 删除第9个item
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav3-content/div[1]/table/tbody/tr[9]/td[3]/button[3]').click()
        # 确定删除弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test3_departCancel")
    def test3_departCancel(self):
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 系统管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[11]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('组织部门管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 选择要删除的班组
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/ol/li[2]/div/span').click()
        # 删除部门下的班组
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/div/table/tbody/tr/td[4]/button[3]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()
        # 选择要删除的部门
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[1]/div/ol/li/div/span').click()
        # 删除部门
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="box"]/div[2]/div/table/tbody/tr[2]/td[4]/button[3]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test4_detectionBuild")
    def test4_detectionCancel(self):
        # *******************创建设备***********************
        # 资源管理
        # ********************巡检项管理新增******************
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
        # 资源管理
        sleep(2)
        self.browser.find_element_by_link_text('检测项管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 删除默认第一个巡检项
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[1]/div/div/div/table/tbody/tr[1]/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/index-header/div/div[2]/div[2]/nav5-content/div[6]/div/div/div[3]/button[1]').click()
        # 点选模板管理
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/span[2]').click()
        # 删除第一个模板item
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/nav5-content/div[1]/div[2]/table/tbody/tr/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/index-header/div/div[2]/div[2]/nav5-content/div[7]/div/div/div[3]/button[1]').click()

    # @unittest.skip("直接跳过测试test5_equipmentTypeCancel")
    def test5_equipmentTypeCancel(self):
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('设备类型管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 选择要删除的item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[2]').click()
        # 确认删除弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test6_equipmentCancel")
    def test6_equipmentCancel(self):
        # *******************新增配电室***********************
        # 资源管理
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
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
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/nav6-content/div[1]/div/div[2]/div/table/tbody/tr/td[6]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div/div[2]/div[2]/nav6-content/div[5]/div/div/div[3]/button[1]').click()
        # 选取配电室item
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/div/span').click()
        sleep(1)
        # 删除配电室
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/nav6-content/div[1]/div/div[2]/div/table/tbody/tr[4]/td[3]/button[2]').click()
        # 确认弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test7_planCancel")
    def test7_planCancel(self):
        # 计划管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[6]/div[1]/i').click()
        sleep(1)
        # 删除第4个item
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/plan-table/div[1]/table/tbody/tr[4]/td[3]/button[2]').click()
        # 确定弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test8_taskCancel")
    def test8_taskCancel(self):
        # 任务管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[7]/div[1]/i').click()
        sleep(1)
        # 删除第4个item
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[7]/button[2]').click()
        # 确定弹出框
        sleep(1)
        self.browser.find_element_by_id('ensure').click()

    # @unittest.skip("直接跳过测试test9_safeBagBuild")
    def test9_safeBagCancel(self):
        # 安全包管理
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[9]/div[1]/i').click()
        sleep(1)
        # 新建
        sleep(1)
        # 删除第一个item
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[3]').click()
        sleep(1)


if __name__ == "__main__":
    unittest.main()
