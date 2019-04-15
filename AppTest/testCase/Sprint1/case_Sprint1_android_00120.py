#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


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
        u"""手机号码输入中文空格"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("进入注册界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)

        logger.info("输入手机号")
        BaseOperate.wait(self, 3)
        BaseOperate.sendTextById(self, PhoneControl.register_phone_num, "     ")

        logger.info("判断是否可以输入超过11位")
        get_text_result = BaseOperate.get_text_by_id(self, PhoneControl.id_warning_tv)
        self.assertTrue(get_text_result == "请输入11位电话号码")



    
