#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
# import warnings
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
        u"""忘记密码输入前5位或后5位验证码正确数字"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入登录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("点击忘记密码")
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phoneNum)

        logger.info("点击获取验证码")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        old_identcode = BaseOperate.get_identifying_code(self, phoneNum)

        logger.info("输入验证码的前五位")
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, old_identcode[:-1])
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        text_1 = BaseOperate.find_toast(self, "请输入正确的短信验证码")
        self.assertTrue(text_1)

        logger.info("输入验证码的后五位")
        BaseOperate.sendTextById(self, PhoneControl.forget_verify_input, old_identcode[1:])
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        text_2 = BaseOperate.find_toast(self, "请输入正确的短信验证码")
        self.assertTrue(text_2)



    
