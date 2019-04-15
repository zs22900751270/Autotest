#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
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
        u"""我的资料没有保存返回上页"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("APP登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("判断姓名是否修改成功")
        old_real_name = BaseOperate.get_text_by_id(self, PhoneControl.id_true_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_true_name)
        BaseOperate.clear_text_by_id(self, PhoneControl.id_infor_modify)
        BaseOperate.go_back(self)
        new_real_name = BaseOperate.get_text_by_id(self, PhoneControl.id_true_name)
        self.assertTrue(old_real_name == new_real_name)



    
