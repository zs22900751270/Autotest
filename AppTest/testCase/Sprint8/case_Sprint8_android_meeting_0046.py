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
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—会议列表界面筛选“已结束/已取消/不参加的”"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击创建会议")
        BaseOperate.creat_meeting(self, "meeting_cancel", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_not_join", "content", "area")
        BaseOperate.creat_meeting(self, "meeting_over", "content", "area")

        logger.info("进行修改会议时间")
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "minute", 5)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_cancel", Content.register_count)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_not_join", Content.register_count)
        s_time, e_time = BaseOperate.get_start_and_end_time(self, "hour", -2)
        BaseOperate.modify_meeting_time(self, s_time, e_time, "meeting_over", Content.register_count)

        logger.info("判断会议是否创建成功")
        title_name = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        BaseOperate.swipe(self, "up")
        title_name1 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_title)
        for i in title_name1:
            if i not in title_name:
                title_name.append(i)
        logger.info(title_name)
        check_can = BaseOperate.check_text_in_list(self, title_name, "meeting_cancel")
        check_not = BaseOperate.check_text_in_list(self, title_name, "meeting_not_join")
        check_over = BaseOperate.check_text_in_list(self, title_name, "meeting_over")
        self.assertTrue(check_can)
        self.assertTrue(check_not)
        self.assertTrue(check_over)

        logger.info("进入会议详情, 取消该会议")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "meeting_cancel")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "取消会议")
        BaseOperate.sendTextById(self, PhoneControl.id_input, "cancel_reason")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("查看是否取消成功")
        status = BaseOperate.get_text_by_id(self, PhoneControl.id_status)
        self.assertEqual(status, "已取消")

        logger.info("切换账号")
        BaseOperate.app_login_out(self)
        BaseOperate.app_login(self, Content.spare_count, Content.spare_password)

        logger.info("点击小秘, 进入会议界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_workLayout)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "会议")

        logger.info("点击进入会议详情,选择不参加会议")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "meeting_not_join")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "不参加")
        BaseOperate.sendTextById(self, PhoneControl.id_input, "not_join_reason")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.go_back(self)

        logger.info("进入“已取消/已结束/不参与”界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_spinner)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_tv_tinted_spinner, 1)

        logger.info("获取会议状态")
        status_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_status)
        BaseOperate.swipe(self, "up")
        status_list1 = BaseOperate.get_text_list_by_id(self, PhoneControl.id_status)
        for i in status_list1:
            if i not in status_list:
                status_list.append(i)
        logger.info(status_list)
        can_res = BaseOperate.check_text_in_list(self, status_list, "已取消")
        not_join_res = BaseOperate.check_text_in_list(self, status_list, "不参与")
        over_res = BaseOperate.check_text_in_list(self, status_list, "已结束")
        self.assertTrue(can_res)
        self.assertTrue(not_join_res)
        self.assertTrue(over_res)


 
     
