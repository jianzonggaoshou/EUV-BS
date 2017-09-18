# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSPlanBuild(unittest.TestCase):
    """BS端增加计划"""
    # 变量赋值
    a = 'test'
    plan = u'日计划测试' + a

    def setUp(self):
        print("start"),
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.browser.maximize_window()
        self.browser.get("http://172.16.40.240:8888/sitopeuv")
        sleep(3)
        # 登录密码
        self.browser.find_element_by_id('userName').clear()
        self.browser.find_element_by_id('userName').send_keys('zhenzhen')
        self.browser.find_element_by_id('userPwd').clear()
        self.browser.find_element_by_id('userPwd').send_keys('123456')
        # 登录
        self.browser.find_element_by_xpath('//input[@value="登录"]').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(10)
        self.browser.quit()

    def test7_BSPlanBuild(self):
        """BS端增加计划"""
        # 计划管理
        self.browser.find_element_by_xpath('//div[@expander-title="计划管理"]').click()
        sleep(1)
        # 新增
        sleep(2)
        self.browser.find_element_by_xpath('//p[@class="titletop"]/button').click()
        #self.browser.find_element_by_xpath(
            #'/html/body/div/index-header/div/div[2]/div[2]/plan-table/div[1]/p/button').click()
        # 表单
        sleep(1)
        # 计划名称
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[1]/input').send_keys(
            BSPlanBuild.plan)
        # 周期类型
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[2]/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[2]/select/option[2]').click()
        # 开始时间
        # 时
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[1]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[1]/option[10]').click()
        # 分
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[2]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[2]/option[2]').click()
        # 秒
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[3]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[3]/select[3]/option[2]').click()
        # 结束时间
        # 时
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[1]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[1]/option[19]').click()
        # 分
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[2]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[2]/option[2]').click()
        # 秒
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[3]').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[4]/select[3]/option[2]').click()

        # 选择班组
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[5]/div/div/div/button').click()
        sleep(1)
        self.browser.find_element_by_link_text('运行一班').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[5]/div/div/div/button').click()
        # 是否激活
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[2]/div/div/div[6]/input').click()

        # 选择安全包
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[7]/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[7]/select/option[2]').click()

        # 计划描述
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[8]/textarea').send_keys(
            u'日计划测试test')

        # 选择设备
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/input').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="tree-root"]/ol/li/ol/li[1]/ol/li[1]/div/span').click()

        # 选择模板
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[9]/div[2]/span/select').click()
        sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/div/div/div[9]/div[2]/span/select/option[2]').click()

        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)

        # 提交
        self.browser.find_element_by_xpath('//*[@id="footer"]/button[1]').click()

        # 断言页面上新添加的元素是否和断言一致
        sleep(3)
        resultPlan = self.browser.find_element_by_xpath(
            '/html/body/div/index-header/div/div[2]/div[2]/plan-table/div[1]/table/tbody/tr[4]/td[1]').text
        # 去除文件中含有的空格等符号
        resultPlan = resultPlan.strip()
        print(resultPlan),
        sleep(1)
        self.assertEqual(resultPlan, u'日计划测试test', msg="添加的日计划模板与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
