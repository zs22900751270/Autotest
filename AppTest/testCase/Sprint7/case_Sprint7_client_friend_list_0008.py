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
        Common.quit(self)

    def test_step(self):
        u"""添加好友界面输入电话号码精确查找好友"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("清除好友关系")
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入通讯录界面")
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("判断是否进入通讯录界面")
        text_list = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res = Common.check_text_in_list(self, text_list, "添加好友")
        self.assertTrue(res)

        logger.info("再添加好友界面搜索未添加好友的账号")
        Common.search_friend_by_name(self, Content.spare_count)

        logger.info("判断搜索结果是否出现‘添加’")
        self.assertTrue(Common.check_if_id_exist(self, ID.openValidateModalBtn))

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击重新进入通讯录界面")
        Common.back(self)
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("再添加好友界面搜索已添加好友的账号")
        Common.search_friend_by_name(self, Content.spare_count)

        logger.info("判断搜索结果是否出现‘已添加’")
        text_list = Common.get_text_by_class_name(self, ClassName.status, "div")
        self.assertTrue(Common.check_text_in_list(self, text_list, "已添加"))


