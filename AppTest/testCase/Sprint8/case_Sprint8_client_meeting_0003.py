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
        u"""未结束的会议列表内容显示"""
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

        logger.info("创建一个会议")
        Common.creat_meeting(self, "meeting_theme")
        start_time, end_time = Common.get_start_and_end_time(self)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_theme", Content.register_count)

        logger.info("进入会议详情界面")
        Common.open_meeting_detail_by_name(self, "meeting_theme", 1)

        logger.info("判断参数项是否正确")
        para_list = Common.get_text_by_class_name(self, ClassName.tit)
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议主题"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议议题"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议创建人"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议开始时间"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议结束时间"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议地点"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "会议创建时间"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "参会人员"))
        self.assertTrue(Common.check_text_in_list(self, para_list, "提醒方式"))


 
     
