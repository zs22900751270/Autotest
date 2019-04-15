#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.del_friend_request_by_sql(self, Content.spare_count)
        Common.del_friend_request_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""搜索已添加好友的部分电话或者部分名称时"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("清除好友关系")
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入通讯录界面")
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("判断是否进入通讯录界面")
        text_list = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res = Common.check_text_in_list(self, text_list, "添加好友")
        self.assertTrue(res)

        logger.info("点击新的朋友")
        new_friend = Common.get_result_by_class_name(self, ClassName.new_friend)
        Common.touch_tag_name_by_element(self, new_friend, "span")

        logger.info("判断是否进入新的朋友界面")
        guide_info = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res1 = Common.check_text_in_list(self, guide_info, "新的朋友")
        self.assertTrue(res1)

        logger.info("点击返回")
        Common.touch_by_id(self, ID.backBtn)

        logger.info("判断是否返回添加好友界面")
        per_page = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res11 = Common.check_text_in_list(self, per_page, "添加好友")
        self.assertTrue(res11)


