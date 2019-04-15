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
        u"""好友资料其他资料显示"""
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

        logger.info("点击查看好友信息")
        Common.touch_text_by_class_name(self, ClassName.name, Content.spare_count_realname, "span")
        f_d = Common.get_text_by_class_name(self, ClassName.text, "section")
        logger.info(f_d)

        logger.info("从后台获取信息")
        mail = Common.get_info_by_sql(self, "select email from user where phone='%s'" % Content.spare_count, "scap")
        logger.info(mail)

        logger.info("进行对比")
        res1 = Common.check_text_in_list(self, f_d, mail)
        res2 = Common.check_text_in_list(self, f_d, Content.spare_count)
        self.assertTrue(res1)
        self.assertTrue(res2)


 
    
