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
        u"""未登录时点击通讯录，跳转登录"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("点击进行登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("判断是否跳转至登录界面")
        result = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertTrue(result == "通讯录")



    
