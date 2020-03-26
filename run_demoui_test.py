#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Syq'

import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from package.HTMLTestRunner import HTMLTestRunner
from public.models.newReport import new_report
from public.models.sendmail import send_mail
import smtplib
smtplib.SMTP_SSL(host='smtp.gmail.com').connect(host='smtp.gmail.com', port=465)


# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):
    os.makedirs(setting.TEST_REPORT + '/' + "screenshot")


"""unittest 框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z,a~z 
如果要让某个测试用例先执行，不能使用默认的main()方法，需要通过TestSuite类的addTest（）方法按照一定的顺序来加载
"""
def add_case(test_path=setting.TEST_DIR):
    """加载所有的测试用例"""
    #discover：找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名时才加载
    # *_sta.py是用例前缀，找到所有后缀为——sta.py（在testcase中）
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*_sta.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='UI自动化测试报告',
                            description='环境：windows 10 浏览器：chrome',
                            tester='Syq')
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)