#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""未登录时，点击‘审批通知’跳转登录"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("未登录时点击消息通知")
        BaseOperate.touchById(self, PhoneControl.id_shenpi)

        logger.info("判断是否跳转至登录界面")
        result = BaseOperate.checkIfIdExist(self, PhoneControl.login_login_button)
        self.assertTrue(result)



    
