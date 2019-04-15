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
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("点击进入忘记密码界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)

        logger.info("点击获取验证码并输入")
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phoneNum)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        identcode = BaseOperate.get_identifying_code(self, phoneNum)
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, identcode)
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/next_btn")
        # 输入特殊字符密码(通过点击键盘坐标)
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/password_tel_num", "       ")
        # 再次输入密码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/password_verify_code_edit", "       ")
        # 点击下一步
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/password_next_btn")
        # 修改成功进入登录界面
        get_text_result = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/password_warning_tv")
        self.assertTrue(get_text_result == "请输入数字字母组合")

