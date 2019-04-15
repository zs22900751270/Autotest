#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
phoneNum = Content.register_count
password = Content.login_password
no_register_count = Content.no_register_count


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
        # 在手机号码框输入特殊字符
        # BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", phoneNum + "123")
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/tel_num")
        BaseOperate.wait(self, 1)
        # 点击键盘上的星号键
        for i in range(6):
            BaseOperate.click_by_coordinate(self, 65, 1440)
            BaseOperate.wait(self, 1)
        # 无法输入
        reslut_input_num_ = BaseOperate.get_text_by_id(self, "com.hqd.app_manager:id/tel_num")
        # 判断是否可以输入
        self.assertTrue(reslut_input_num_ == "请输入手机号码")



    
