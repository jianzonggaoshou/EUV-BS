# coding=utf-8
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
import sys
import time
from HTMLTestRunner import HTMLTestRunner

reload(sys)
sys.setdefaultencoding('utf-8')

# 生成HTML文件
test_dir = 'C:\\Users\\xuzhen\\PycharmProjects\\EUV-BS\\EUV\\BS'
report_dir = 'C:\\Users\\xuzhen\\PycharmProjects\\EUV-BS\\EUV\\BS\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = report_dir + '/' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='EUV-BS端自动化测试报告', description='用例执行情况：')
runner.run(discover)
fp.close()

# 排序
lists = os.listdir(report_dir)

lists.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
print(lists[-1])
file = os.path.join(report_dir, lists[-1])
print(file)

# 发送邮箱服务器
smtpserver = 'smtp.si-top.com'

# 发送邮箱用户/密码
user = 'gaokun@si-top.com'
password = '123Li456'

# 发送邮箱
sender = 'gaokun@si-top.com'

# 接收邮箱
receiver = 'xuzhen@si-top.com'

# 发送邮件主题
subject = 'EUV AutoTest email'

# 发送的附件
sendFile = open(file, 'rb').read()

# 发送邮件主题
msg = MIMEMultipart()
msg['subject'] = Header(subject, 'utf-8')

# 编写HTML类型的邮件正文
f = open(file, 'rb')
mail_body = f.read()
f.close()

text = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(text)

# 编写附件
attachment = MIMEText(sendFile, 'base64', 'utf-8')
attachment["Content-Type"] = 'application/octet-stream'
attachment["Content-Disposition"] = 'attachment; filename="EUVTestReport.html"'

msg.attach(attachment)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
