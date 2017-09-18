# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class BSEquipmentBuild(unittest.TestCase):
    """BS端增加台账"""
    # 变量赋值
    a = 'test'
    room = u'配电室' + a
    transformer = u'变压器' + a

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
        print("end")
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
        self.browser.find_element_by_xpath('//div[@expander-title="资源管理"]').click()
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
        self.browser.find_element_by_id('roomName').send_keys(BSEquipmentBuild.room)
        self.browser.find_element_by_id('roomType').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="roomType"]/option[2]').click()
        self.browser.find_element_by_id('roomRemark').send_keys(u'备注test')
        # 确定
        self.browser.find_element_by_id('newR-save').click()

        # *******************新增设备***********************
        sleep(2)
        self.browser.find_element_by_id('newEquipment').click()
        # 表单
        # 设备名称
        sleep(1)
        self.browser.find_element_by_id('equipmentName').send_keys(BSEquipmentBuild.transformer)
        # 设备类型
        sleep(1)
        self.browser.find_element_by_id('equipmentTypeId').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="equipmentTypeId"]/option[2]').click()
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
        self.browser.find_element_by_id('equipmentRemark').send_keys(u'备注test')
        # 确定
        sleep(1)
        self.browser.find_element_by_id('newE-save').click()

        # 断言页面上新添加的元素是否和断言一致
        # 点击公司
        sleep(3)
        self.browser.find_element_by_xpath('//span[@title="自动化测试脚本"]').click()
        sleep(1)
        resultRoom = self.browser.find_elements_by_xpath('//td[@data-title-text="配电室名称"]')[0].text
        print(resultRoom),
        sleep(1)
        self.browser.find_element_by_xpath('//span[@title="配电室test"]').click()
        resultTransformer = self.browser.find_elements_by_xpath('//td[@data-title-text="设备名称"]')[0].text
        print(resultTransformer)
        sleep(1)
        self.assertEqual(resultRoom, u'配电室test', msg="添加的配电室与网页上显示的不同！")
        self.assertEqual(resultTransformer, u'变压器test', msg="添加的设备与网页上显示的不同！")


if __name__ == '__main__':
    unittest.main()
