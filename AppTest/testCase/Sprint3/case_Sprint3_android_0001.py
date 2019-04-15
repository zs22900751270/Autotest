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
        u"""输入正确的手机号码和密码，验证码图片不出现"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)

        logger.info("点击登录或注册")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)

        logger.info("输入账号")
        BaseOperate.sendTextById(self, PhoneControl.login_count, phoneNum)

        logger.info("输入密码")
        BaseOperate.sendTextById(self, PhoneControl.login_password, password)

        logger.info("检测是否有验证码出现")
        result = BaseOperate.checkIfIdExist(self, PhoneControl.id_verify_code_content)
        self.assertFalse(result)

        logger.info("点击登录")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_login_button)


 

