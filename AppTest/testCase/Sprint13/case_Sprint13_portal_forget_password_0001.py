#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""PC—后端进入忘记密码界面"""
        logger.info("点击修改密码")
        fgt_psd = Common.get_element_by_class_name_and_text(self, "a", "", "忘记密码")
        Common.touch_by_element(self, fgt_psd)

        logger.info("查看是否进入修改密码界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.checkUpdatePwdcodeBtn))
