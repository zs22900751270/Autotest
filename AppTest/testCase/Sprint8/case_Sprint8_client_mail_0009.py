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
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""PC收件箱标题主题显示"""
        logger.info("清空邮箱")
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)

        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("创建好友关系,清空收件人邮箱账号")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)

        logger.info("进入邮箱界面")
        Common.touch_text_by_class_name(self, ClassName.center, "邮箱", "p")

        logger.info("判断是否进入邮箱详情界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "邮箱"))

        logger.info("发送邮件")
        Mail.send_mail(self, Content.spare_count, mail_theme="mail_theme1")

        logger.info("切换账号")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入邮箱界面")
        Common.touch_text_by_class_name(self, ClassName.center, "邮箱", "p")

        logger.info("判断是否进入邮箱详情界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "邮箱"))

        logger.info("判断数量是否出现变化")
        i = 0
        res = True
        while i <= 120:
            logger.info(Common.get_text_by_class_name(self, ClassName.mail_title_content)[0])
            if Common.get_text_by_class_name(self, ClassName.mail_title_content)[0] == "(共 1 封,其中 未读邮件 1 封)":
                res = True
                break
            else:
                logger.info("网络有延迟，收件较慢，请等待。。。。。。。")
                Common.wait(self, 1)
                i = i+1
            res = False
        self.assertTrue(res)

        logger.info("查看收件主题")
        mail_theme = Common.get_text_by_class_name(self, ClassName.td_content_sp, "span")
        self.assertTrue(Common.check_text_in_list(self, mail_theme, "mail_theme1"))

