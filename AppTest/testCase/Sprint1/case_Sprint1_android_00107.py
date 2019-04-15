#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
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

        logger.info("进入注册界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)

        logger.info("输入手机号，获取验证码")
        BaseOperate.sendTextById(self, PhoneControl.register_phone_num, Content.no_register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_verify_button)
        identify_code = BaseOperate.get_identifying_code(self, no_register_count)

        logger.info("输入前五位验证码")
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, identify_code[:-1])

        logger.info("点击下一步")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        get_toast = BaseOperate.find_toast(self, "请输入正确的短信验证码")
        self.assertTrue(get_toast)

        logger.info("输入后五位验证码")
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, identify_code[1:])

        logger.info("点击下一步")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        get_toast = BaseOperate.find_toast(self, "请输入正确的短信验证码")
        self.assertTrue(get_toast)



    
