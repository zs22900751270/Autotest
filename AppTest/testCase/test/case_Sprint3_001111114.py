#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        # browse = BrowserEngine(self)
        # self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        """"""
        # Common.report_screen_shot(self, self.case_name)
        # Common.quit(self)

    def test_step(self):
        u"""test step"""
        Interface.modify_phone_num(self, "18888888888", "zs123456", "19802990115")
        pass


