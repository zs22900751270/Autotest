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
        BaseOperate.modify_password_by_phone(self, Content.register_count, Content.login_password)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""输入正确的确认密码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击忘记密码")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phoneNum)

        logger.info("点击获取验证码")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        BaseOperate.wait(self, 5)
        old_identcode = BaseOperate.get_identifying_code(self, phoneNum)

        logger.info("输入验证码")
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, old_identcode)

        logger.info("两次输入密码")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn)
        BaseOperate.sendTextById(self, PhoneControl.id_password_tel_num, "qwe123")
        BaseOperate.sendTextById(self, PhoneControl.id_password_verify_code_edit, "qwe123")

        logger.info("点击下一步")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_password_next_btn)

        logger.info("判断是否修改成功")
        first_result = BaseOperate.get_text_by_id(self, PhoneControl.id_next_btn)
        self.assertEqual(first_result, "登录")



    
