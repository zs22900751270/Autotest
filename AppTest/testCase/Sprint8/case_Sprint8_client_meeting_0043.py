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
        u"""异常情况与会人在点会议开始后点击签到前1秒创建人取消会议"""
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

        logger.info("创建多个会议")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        Common.creat_meeting(self, "meeting_theme", name=real_name)

        logger.info("通过后台修改会议时间")
        start_time, end_time = Common.get_start_and_end_time(self, time_len=10)
        Common.modify_meeting_time(self, start_time, end_time, "meeting_theme", Content.register_count)

        logger.info("登录参会人账号")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "会议", "p")

        logger.info("进入会议详情界面")
        Common.open_meeting_detail_by_name(self, "meeting_theme", 1)

        logger.info("点击确认参加会议")
        Common.touch_by_id(self, ID.attendBtn)

        logger.info("取消会议")
        Common.modify_meeting_status_by_sql(self, Content.register_count, "meeting_theme")

        logger.info("点击签到")
        Common.touch_by_id(self, ID.signMeetingBtn)

        logger.info("提示会议已取消")
        tip_text = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.sweet_alert_showsweetalert_visible, "div"))
        self.assertTrue(Common.check_text_in_list(self, tip_text, "会议已取消"))


 
     
