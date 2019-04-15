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
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.quit(self)

    def test_step(self):
        u"""搜索已添加好友的部分电话或者部分名称时"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("清除好友关系")
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("修改好友真实姓名")
        Common.rename_user_realname_by_phone(self, Content.spare_count_realname, Content.spare_count)

        logger.info("点击进入通讯录界面")
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("判断是否进入通讯录界面")
        text_list = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res = Common.check_text_in_list(self, text_list, "添加好友")
        self.assertTrue(res)

        logger.info("在左侧通讯录搜索已添加好友的部分姓名")
        Common.search_friend_by_name(self, Content.spare_count_realname[:-3], False)

        logger.info("判断是否搜索成功")
        self.assertEqual(len(Common.get_search_friend_results(self, False)), 1)

        logger.info("在左侧通讯录搜索已添加好友的部分电话")
        Common.search_friend_by_name(self, Content.spare_count[:-1], False)

        logger.info("判断是否搜索成功")
        self.assertEqual(len(Common.get_search_friend_results(self, False)), 1)


 

