#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        u"""在通讯录界面搜索好友"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("点击进行登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touchById(self, PhoneControl.id_me_icon)

        logger.info("进入我的头像")
        BaseOperate.touchById(self, PhoneControl.id_profile_layout)

        logger.info("点击选择图片")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "选择图片")

        logger.info("判断是否进入选择图片界面")
        text = BaseOperate.get_text_by_id(self, PhoneControl.id_head_actionmode_title)
        self.assertEqual(text, "选择图片")

        logger.info("点击返回按钮")
        BaseOperate.touchById(self, PhoneControl.id_head_select_left)

        logger.info("判断是否返回成功")
        text = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual("个人资料", text)


