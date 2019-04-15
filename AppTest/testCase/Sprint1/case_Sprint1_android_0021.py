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
        u"""test step"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)

        logger.info("登录app, 并进入个人资料界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("判断自动授权是否开启")
        element = self.driver.find_element_by_id(PhoneControl.my_data_authorization_switch_button)
        status = element.get_attribute("checked")
        self.assertTrue(status == "true")

        logger.info("点击关闭自动授权,选择取消")
        element.click()
        BaseOperate.touch_id_by_index(self, "android:id/button2")
        BaseOperate.wait(self, 2)
        status = element.get_attribute("checked")
        self.assertTrue(status == "true")



    
