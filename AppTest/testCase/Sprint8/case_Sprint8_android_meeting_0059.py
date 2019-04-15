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
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.delete_meeting_record(self, Content.register_count)
        BaseOperate.delete_meeting_record(self, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—未结束的会议，自动标记已结束"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.creat_meeting(self, "meeting_test", "content", "area")

        logger.info("进行修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "hour", -2)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_test", Content.register_count)

        logger.info("判断是否已标记为已结束")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_spinner)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_tv_tinted_spinner, 2)
        status_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_status)
        check_1 = BaseOperate.check_text_in_list(self, status_list, "已结束")
        self.assertEqual(len(status_list), 1)
        self.assertTrue(check_1)
        

 
     
