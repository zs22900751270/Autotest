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
        u"""预约会议参会人显示"""
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

        logger.info("点击创建会议")
        Common.touch_by_id(self, ID.addMeetingBtn)
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        add_person = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, add_person, "img")
        name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
        Common.touch_text_by_elements(self, name_list, real_name)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看参会人提示")
        err_list = Common.get_text_by_class_name(self, ClassName.name, "p")
        self.assertTrue(Common.check_text_in_list(self, err_list, real_name))


 
     
