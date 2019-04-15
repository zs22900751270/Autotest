#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


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
        u"""分组名称长度限制"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录APP，进入主界面")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入首页")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击分组联系人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_group)

        logger.info("判断是否进入分组联系人界面")
        text = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text, "分组联系人")

        logger.info("创建分组联系人")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("输入分组名称")
        BaseOperate.sendTextById(self, PhoneControl.id_group_name, "1234567890123456789011111")

        logger.info("判断分组名称长度")
        text = BaseOperate.get_text_by_id(self, PhoneControl.id_group_name)
        self.assertTrue(len(text) < len("1234567890123456789011111"))


 

