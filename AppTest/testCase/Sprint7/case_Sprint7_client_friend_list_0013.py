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
        Common.connect_sql(self, "update scap.user set realname='%s' where phone='%s'" %
                           (Content.spare_count_realname, Content.spare_count), "scap")
        Common.quit(self)

    def test_step(self):
        u"""已添加的好友名称首位为特殊字符字符时，排序"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("清除好友关系")
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("判断好友名称开头为特殊字符")
        Common.connect_sql(self, "UPDATE scap.user SET realname='@$qweqwe' WHERE phone='%s'" % Content.spare_count,
                           "scap")

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入通讯录界面")
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("判断该好友是否排列在最后")
        name_list = Common.get_text_by_class_name(self, ClassName.letter_wrap, "div")
        logger.info(name_list)
        result = False
        for i in name_list:
            if "@$qweqwe" in i and "@" in i:
                result = True
                break
        self.assertTrue(result)


 
    
