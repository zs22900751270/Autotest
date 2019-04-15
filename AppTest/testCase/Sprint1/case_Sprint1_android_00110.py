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
        BaseOperate.wait(self, 5)
        # 点击我的
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        # 点击登录或注册
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        # 点击注册
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)
        # 输入手机号码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", no_register_count)

        # 空格在开头输入验证码
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/verify_code_edit")
        # 点击手机键盘上面的空格
        for i in range(6):
            BaseOperate.click_by_coordinate(self, 750, 1700)
            BaseOperate.wait(self, 1)
        # 是否可以输入空格
        get_input_identify1 = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/verify_code_edit")
        logger.info(get_input_identify1)
        self.assertTrue(get_input_identify1 == "请输入验证码")



    
