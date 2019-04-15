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
        u"""与会人点击已结束、已取消、不参与的列表中的已取消的"""
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

        logger.info("创建一个个会议")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        Common.creat_meeting(self, "meeting_over", name=real_name)

        logger.info("取消会议")
        logger.info("取消其中一个会议")
        Common.open_meeting_detail_by_name(self, "meeting_over", 1)
        Common.touch_by_id(self, ID.openCancelModelBtn)
        reason = Common.get_results_by_class_name_blank(self, "textarea", ClassName.ivu_input)
        Common.send_text_by_element(self, reason[-1], "1234")
        Common.touch_by_id(self, ID.cancelMeetingBtn)

        logger.info("登录参会人账号")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "会议", "p")

        logger.info("进入已取消/已完成/不参见界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "会议", "a")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "已结束/已取消/不参与的")

        logger.info("查看会议是否都存在该分类中")
        self.assertTrue(Common.check_meeting_belong_to(self, "meeting_over", 2))

        logger.info("进入会议详情界面")
        Common.open_meeting_detail_by_name(self, "meeting_over", 2)

        logger.info("判断删除按钮是否存在")
        self.assertTrue(Common.check_if_id_exist(self, ID.deleteMeetingBtn))

        logger.info("点击删除会议")
        Common.touch_by_id(self, ID.deleteMeetingBtn)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看会议是否都存在该分类中")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "已结束/已取消/不参与的")
        self.assertFalse(Common.check_meeting_belong_to(self, "meeting_over", 2))
        self.assertFalse(Common.check_meeting_belong_to(self, "meeting_over", 3))


 
     
