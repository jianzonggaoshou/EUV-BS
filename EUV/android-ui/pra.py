# coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0.0',
    'deviceName': 'AndroidReal',
    'appPackage': 'com.sito.evpro.inspection.test',
    'appActivity': 'com.sito.evpro.inspection.view.splash.SplashActivity',
    # 'appWaitActivity': '.view.splash.SplashActivity',
    'noReset': 'True',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True',
    }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 登录
sleep(3)
driver.find_element_by_id('com.sito.evpro.inspection:id/edit_username').clear()
driver.find_element_by_id('com.sito.evpro.inspection:id/edit_username').set_value('xujianzuyuan')
driver.find_element_by_id('com.sito.evpro.inspection:id/edit_password').clear()
driver.find_element_by_id('com.sito.evpro.inspection:id/edit_password').send_keys('123456')
driver.find_element_by_id('com.sito.evpro.inspection:id/tv_login').click()

# 故障上报
sleep(1)
driver.find_element_by_id('com.sito.evpro.inspection:id/tv_fault').click()
sleep(1)
driver.find_element_by_id('com.sito.evpro.inspection:id/id_fault_devicename').click()




sleep(500)
driver.quit()