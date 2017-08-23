# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class BSAddTest(unittest.TestCase):
    """BS端增加测试"""
    # 变量赋值
    a = 'test'
    room = u'配电室' + a
    transformer = u'变压器' + a

    def setUp(self):
        print("test6 case start"),
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
        print("test6 case end")
        sleep(10)
        self.browser.quit()

    def test6_BSEquipmentBuild(self):
        """BS端增加台账"""
        # *******************新增配电室***********************
        # 滚动翻页
        js = "window.scrollTo(0, 500)"
        self.browser.execute_script(js)
        sleep(3)
        # 资源管理
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/index-header/div/div[2]/div[1]/div/div[12]/div[1]/i').click()
        sleep(1)
        self.browser.find_element_by_link_text('台账管理').click()
        # 滚动翻页
        js = "window.scrollTo(0, 0)"
        self.browser.execute_script(js)
        sleep(3)
        # 新增配电室
        sleep(2)
        self.browser.find_element_by_id('newRoom').click()
        sleep(1)
        self.browser.find_element_by_id('roomName').send_keys(BSAddTest.room)
        self.browser.find_element_by_id('roomRemark').send_keys(u'配电室test')
        # 确定
        self.browser.find_element_by_id('newR-save').click()

        # *******************新增设备***********************
        sleep(2)
        self.browser.find_element_by_id('newEquipment').click()
        # 表单
        # 设备名称
        sleep(1)
        self.browser.find_element_by_id('equipmentName').send_keys(BSAddTest.transformer)
        # 设备类型
        sleep(1)
        self.browser.find_element_by_id('equipmentTypeId').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="equipmentTypeId"]/option[5]').click()
        # 配电室
        sleep(1)
        self.browser.find_element_by_id('roomId').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="roomId"]/option[2]').click()
        # 设备编号
        sleep(1)
        self.browser.find_element_by_id('equipmentSn').send_keys(u'生产编号number1')
        # 出厂编号
        sleep(1)
        self.browser.find_element_by_id('equipmentFsn').send_keys(u'出厂编号number1')
        # 生产厂商
        sleep(1)
        self.browser.find_element_by_id('manufacturer').send_keys(u'生产厂家number1')
        # 供应厂商
        sleep(1)
        self.browser.find_element_by_id('supplier').send_keys(u'供应厂商number1')
        # 运行状态
        sleep(1)
        self.browser.find_element_by_id('workingState').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="workingState"]/option[10]').click()
        # 设备状态
        sleep(1)
        self.browser.find_element_by_id('equipmentState').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="equipmentState"]/option[2]').click()
        # 备注
        sleep(1)
        self.browser.find_element_by_id('equipmentRemark').send_keys(u'test备注')
        # 确定
        sleep(1)
        self.browser.find_element_by_id('newE-save').click()
        # # 截图
        # sleep(3)
        # now = time.strftime('%y-%m-%d-%H:%M:%S')
        # self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/台账管理%s.jpg' % now)