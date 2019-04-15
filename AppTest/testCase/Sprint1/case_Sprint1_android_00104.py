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
        u"""已用过一次验证码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入注册界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)

        logger.info("获取验证码")
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, no_register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        BaseOperate.wait(self, 5)
        identcode = BaseOperate.get_identifying_code(self, no_register_count)

        logger.info("等待一分钟后，获取验证码")
        BaseOperate.wait(self, 40)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_tel_num)
        BaseOperate.wait(self, 40)
        # 再次通过后台获取验证码
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn)
        BaseOperate.wait(self, 5)
        BaseOperate.get_identifying_code(self, no_register_count)
        # 输入验证码
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, identcode)
        # 点击下一步
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn, t=0)
        self.assertTrue(BaseOperate.find_toast(self, "验证码输入错误"))



    
