#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.delete_meeting_record(self, Content.register_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—待办界面所有事件都可以点击查看详情"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入待办")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("创建多个会议")
        BaseOperate.creat_meeting(self, "meeting_test1", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test2", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test3", "content", "area")

        logger.info("修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 5)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test1", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 10)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test2", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 15)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test3", Content.register_count)

        logger.info("判断是否创建成功,是否按照开始时间排序")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "待办")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        self.assertEqual(theme_list[0], "meeting_test1")
        self.assertEqual(theme_list[1], "meeting_test2")
        self.assertEqual(theme_list[2], "meeting_test3")

        logger.info("点击进入会议详情")
        BaseOperate.touch_text_by_id(self, "meeting_test1", PhoneControl.id_theme)
        logger.info("判断是否进入会议详情")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "会议详情")
        BaseOperate.go_back(self)

        logger.info("点击进入会议详情")
        BaseOperate.touch_text_by_id(self, "meeting_test2", PhoneControl.id_theme)
        logger.info("判断是否进入会议详情")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "会议详情")
        BaseOperate.go_back(self)

        logger.info("点击进入会议详情")
        BaseOperate.touch_text_by_id(self, "meeting_test3", PhoneControl.id_theme)
        logger.info("判断是否进入会议详情")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "会议详情")


 
     
