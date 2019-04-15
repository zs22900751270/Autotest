#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.delete_meeting_record(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""我发出的列表内容状态显示"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "会议", "p")

        logger.info("判断是否进入会议界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.addMeetingBtn))

        logger.info("创建三个个会议")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        logger.info(real_name)
        Common.creat_meeting(self, "meeting_cancel", name=real_name)
        Common.creat_meeting(self, "meeting_over", name=real_name)
        Common.creat_meeting(self, "meeting_no_status", name=real_name)

        logger.info("通过后台修改会议时间")
        start_time, end_time = Common.get_start_and_end_time(self, type="hour", time_len=-2)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_over", Content.register_count)
        start_time, end_time = Common.get_start_and_end_time(self)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_cancel", Content.register_count)
        start_time, end_time = Common.get_start_and_end_time(self, time_len=-5)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_no_status", Content.register_count)

        logger.info("取消其中一个会议")
        Common.open_meeting_detail_by_name(self, "meeting_cancel", 1)
        Common.touch_by_id(self, ID.openCancelModelBtn)
        reason = Common.get_results_by_class_name_blank(self, "textarea", ClassName.ivu_input)
        Common.send_text_by_element(self, reason[-1], "1234")
        Common.touch_by_id(self, ID.cancelMeetingBtn)
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "会议", "a")

        logger.info("进入我发出的界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "我发起的")

        logger.info("查看会议是否都存在该分类中")
        self.assertTrue(Common.check_meeting_belong_to(self, "meeting_cancel", 3))
        self.assertTrue(Common.check_meeting_belong_to(self, "meeting_over", 3))
        self.assertTrue(Common.check_meeting_belong_to(self, "meeting_no_status", 3))


 
     
