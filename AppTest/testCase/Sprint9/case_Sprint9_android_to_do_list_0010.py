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
        u"""android—待办界面所有事件修改开始时间之后，该界面会重新排序"""
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
        BaseOperate.creat_meeting(self, "meeting_test4", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_test5", "content", "area")

        logger.info("修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 5)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test1", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 10)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test2", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 15)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test3", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 20)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test4", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 25)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test5", Content.register_count)

        logger.info("判断是否创建成功,是否按照开始时间排序")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "待办")
        theme_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        BaseOperate.swipe(self, "up")
        theme_list2 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_theme)
        for i in theme_list2:
            if i not in theme_list:
                theme_list.append(i)
        self.assertEqual(len(theme_list), 5)

        for j in range(1, 6):
            self.assertTrue(BaseOperate.check_text_in_list(self, theme_list, "meeting_test%s" % j))


 
     
