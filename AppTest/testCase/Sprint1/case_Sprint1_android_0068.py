#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
# import warnings
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
        # 点击忘记密码
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/login_forget_password")
        # BaseOperate.sendTextById(self, "com.hqd.app_manager:id/verify_code_edit", "      ")
        # 聚焦验证码
        BaseOperate.touch_id_by_index(self,  "com.hqd.app_manager:id/tel_num")
        BaseOperate.wait(self, 2)
        for i in range(6):
            BaseOperate.click_by_coordinate(self, 1000, 1600)
            BaseOperate.wait(self, 1)
        # 获取所输入的验证码
        input_identifying = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/verify_code_edit")
        logger.info(input_identifying)
        input_content = False
        if input_identifying == "请输入验证码":
            input_content = True
        self.assertTrue(input_content)



    
