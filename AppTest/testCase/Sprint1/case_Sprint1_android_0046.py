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
        u"""测试性别选项"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录APP")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入个人资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("设置性别为男")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_sex)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "男")
        logger.info("是否返回我的资料界面并且设置性别成功")
        sex = BaseOperate.get_text_by_id(self, PhoneControl.id_sex)
        self.assertTrue(sex == "男")

        logger.info("设置性别为女")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_sex)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "女")
        logger.info("是否返回我的资料界面并且设置性别成功")
        sex = BaseOperate.get_text_by_id(self, PhoneControl.id_sex)
        self.assertTrue(sex == "女")

        logger.info("设置性别是点击取消")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_sex)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "取消")
        logger.info("是否返回我的资料界面并且设置性别成功")
        sex = BaseOperate.get_text_by_id(self, PhoneControl.id_sex)
        self.assertTrue(sex == "女")



    
