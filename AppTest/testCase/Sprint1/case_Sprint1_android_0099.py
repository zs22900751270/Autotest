#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
no_register_count = Content.no_register_count
phoneNum = Content.register_count
password = Content.login_password
long_password = "zhangsenzhangsenzhangsenzhangsen1234"


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
        # 点击我的
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        # 点击登录或注册
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        # 点击忘记密码
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/login_forget_password")
        # 输入手机号码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/tel_num", phoneNum)
        # 点击获取验证码
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/verify_code_btn")
        # 通过后台获取验证码
        BaseOperate.wait(self, 5)
        identcode = BaseOperate.get_identifying_code(self, phoneNum)
        # 输入验证码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/verify_code_edit", identcode)
        # 点击下一步
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/next_btn")
        # 输入6位以下密码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/password_tel_num", "qwe12")
        # 再次输入密码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/password_verify_code_edit", "qwe12")
        # 点击下一步
        BaseOperate.touch_id_by_index(self, "com.hqd.app_manager:id/password_next_btn", t=0)
        # 修改成功进入登录界面
        get_text_result1 = BaseOperate.find_toast(self, "请输入6位及以上字母数字组合密码")
        self.assertTrue(get_text_result1)

        # 输入32位以上密码
        BaseOperate.sendTextById(self, "com.hqd.app_manager:id/password_tel_num", long_password)
        # 提示不能输入32位长度以上的密码
        get_text_result2 = BaseOperate.find_toast(self, "密码长度最长支持32位")
        self.assertTrue(get_text_result2)
