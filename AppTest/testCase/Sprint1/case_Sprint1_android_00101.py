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
        u"""默认勾选用户协议"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)

        logger.info("输入手机号码, 点击获取验证码")
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, no_register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        identcode = BaseOperate.get_identifying_code(self, no_register_count)

        logger.info("输入验证码，点击下一步")
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, identcode)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn)

        logger.info("检测用户协议是否默认选择")
        parameter = BaseOperate.get_parameter_by_id(self, PhoneControl.id_user_agreement_check, "checked")
        self.assertTrue(parameter == "true")

        logger.info("点击去掉勾选状态")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_user_agreement_check)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_password_next_btn)
        get_toast = BaseOperate.find_toast(self, "请先同意用户协议")
        self.assertTrue(get_toast)

