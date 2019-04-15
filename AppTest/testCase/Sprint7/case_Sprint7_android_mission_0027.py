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
        u"""新建任务提醒选择验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入任务界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "任务")

        logger.info("点击创建任务")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 1)

        logger.info("判断是否进入创建任务界面")
        title_name = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(title_name, "创建任务")

        logger.info("查看默认的提示值为")
        remind_text = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
        self.assertEqual(remind_text, "不提醒")

        logger.info("选择提前1小时")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_option_layout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "截止前1小时")

        logger.info("查看提示时间是否修改成功")
        remind_text = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
        self.assertEqual(remind_text, "截止前1小时")

        logger.info("选择提前3小时")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_option_layout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "截止前3小时")

        logger.info("查看提示时间是否修改成功")
        remind_text = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
        self.assertEqual(remind_text, "截止前3小时")

        logger.info("选择提前1天")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_option_layout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "截止前1天")

        logger.info("查看提示时间是否修改成功")
        remind_text = BaseOperate.get_text_by_id(self, PhoneControl.id_remind_option)
        self.assertEqual(remind_text, "截止前1天")


 
    
