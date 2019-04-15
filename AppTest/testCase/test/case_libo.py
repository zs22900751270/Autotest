#!/usr/bin/env python
# _*_coding:utf-8_*_

import unittest, os
from AppTest.framework import *
url = "https://111.20.159.77/iredadmin/login"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""test step"""
        self.web_driver.find_element_by_id("user").send_keys("zhangyi@yx.cnhqd.net")
        self.web_driver.find_element_by_id("password").send_keys("Hqd123456")
        self.web_driver.find_element_by_name("login").click()
        time.sleep(2)
        Common.touch_by_xpath(self, "/html/body/div[1]/div/div[2]/ul/li[2]")
        Common.touch_by_xpath(self, "//*[@id=\"list_table\"]/table/tbody/tr/td[5]/a/span")
        phone = ['18066755917', '15229332312', '18629391235', '15891291673', '13772933823', '13484487823']
        name = ['李驰', '关瑞婷', '张森（开发）', '马群起', '马庆华', '马庆忠']
        for i in range(len(phone)):
            Common.touch_by_xpath(self, "/html/body/div[3]/div/div/div/div/div[1]/ul/li[2]")
            self.web_driver.find_element_by_name("username").send_keys(phone[i])
            self.web_driver.find_element_by_name("newpw").send_keys("Hqd123456")
            self.web_driver.find_element_by_name("confirmpw").send_keys("Hqd123456")
            self.web_driver.find_element_by_name("cn").send_keys(name[i])
            self.web_driver.find_element_by_name("mailQuota").send_keys("1024")
            Common.touch_by_xpath(self, "//*[@id=\"user_add\"]/form/div[3]/span/input")

            Common.wait(self, 2)
            Common.touch_by_xpath(self, "//*[@id=\"profile_general\"]/form/div[3]/span/input")
            Common.touch_by_xpath(self, "//*[@id=\"breadcrumb\"]/li[3]/a")


if __name__ == "__main__":
    unittest.main()
