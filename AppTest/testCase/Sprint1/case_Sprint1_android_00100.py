#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.modify_password_by_phone(self, Content.register_count, Content.login_password)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)

        logger.info("获取验证码")
        BaseOperate.sendTextById(self, PhoneControl.forget_count, Content.register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_verify_button)
        identcode = BaseOperate.get_identifying_code(self, Content.register_count)

        logger.info("输入验证码，点击下一步")
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, identcode)
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_next_button)
        BaseOperate.wait(self, 1)

        logger.info("输入密码")
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password, "qwer12321rewq")
        BaseOperate.sendTextById(self, PhoneControl.forget_input_password_again, "qwer12321rewq")
        BaseOperate.touch_id_by_index(self, PhoneControl.forget_input_password_next_button)
        BaseOperate.wait(self, 1)

        logger.info("判断是否修改成功")
        first_result = BaseOperate.checkIfIdExist(self, PhoneControl.id_next_btn)
        self.assertTrue(first_result)



    
