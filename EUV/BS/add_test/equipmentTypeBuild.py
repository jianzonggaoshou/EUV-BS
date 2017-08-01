# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


class EquipmentTypeBuild(unittest.TestCase):

	def setUp(self):
		print("equipmentTypeBuild case start"),
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
		print("equipmentTypeBuild case end")
		sleep(10)
		self.browser.quit()

	def test_equipmentTypeBuild(self):
		# 滚动翻页
		js = "window.scrollTo(0, 500)"
		self.browser.execute_script(js)
		sleep(3)
		# 资源管理
		sleep(1)
		self.browser.find_element_by_xpath('/html/body/div[1]/index-header/div[1]/div[1]/div/div[11]/div[1]/i').click()
		sleep(1)
		self.browser.find_element_by_link_text('设备类型管理').click()
		# 滚动翻页
		js = "window.scrollTo(0, 0)"
		self.browser.execute_script(js)
		sleep(3)
		# 新增
		sleep(2)
		self.browser.find_element_by_id('news').click()
		# 表单
		sleep(1)
		self.browser.find_element_by_id('name').send_keys(u'设备类型test')
		self.browser.find_element_by_xpath(
			'/html/body/div/index-header/div[2]/div[2]/div/div/form/div[2]/textarea').send_keys(u'设备类型test')
		# 确定
		self.browser.find_element_by_id('new-save').click()

		# # 截图
		# sleep(3)
		# now = time.strftime('%y-%m-%d-%H:%M:%S')
		# self.browser.get_screenshot_as_file('/Users/xuzhen/PycharmProjects/QA2017/EUV/BS/image/设备类型管理%s.jpg' % now)


if __name__ == "__main__":
	unittest.main()
