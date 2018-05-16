#coding:utf-8

import unittest
import HTMLTestRunner

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def all_case():
    # 待执行用例的目录
    case_dir = "D:\\aaaa\\bbbb\\case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTests(test_case)
    print(testcase)
    return(testcase)


def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，传送D:/软件/yasuo.rar文件
    part = MIMEApplication(open('D:/aaaa/bbbb/report/result.html','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="result.html")
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()


if __name__ == "__main__":
    # 返回实例
    # runner = unittest.TextTestRunner()
    report_path = "D:\\aaaa\\bbbb\\report\\result.html"
    fp = open(report_path, "wb")
    runner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'这是我的自动化测试报告',description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()

    try:
        subject = 'Python 测试邮件'
        content = '这是一封来自 Python 编写的测试邮件。'
        send_email('smtp.163.com', 'yanghaotai@163.com', '15811307862yht', '596532245@qq.com', subject, content)
    except Exception as err:
        print(err)
