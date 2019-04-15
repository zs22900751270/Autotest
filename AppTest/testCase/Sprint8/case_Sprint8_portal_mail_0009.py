#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Mail.modify_mail_enable_status_by_user(self, Content.register_count)
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.quit(self)

    def test_step(self):
        u"""邮箱已经运行了一段时间后停用后再启用，停用期间有邮件发给该用户"""
        logger.info("打开客户端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击进入内置应用界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用", "li")

        logger.info("点击进入邮箱管理界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "邮箱管理", "div")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "邮箱管理", "li")

        logger.info("查看是否进入邮箱管理界面")
        text_list = Common.get_text_by_class_name(self, ClassName.menu_title)
        self.assertTrue(Common.check_text_in_list(self, text_list, "邮箱管理"))

        logger.info("先停用邮箱")
        Mail.open_or_close_mail_by_phone(self, Content.register_count, False)

        logger.info("邮箱停用成功")
        use_status = Mail.get_mail_use_status_by_phone(self, Content.register_count)[0]
        self.assertFalse(use_status)

        logger.info("创建好友关系,清空收件人邮箱账号")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.spare_count)
        Mail.del_mail_record_by_user(self, Content.register_count)

        logger.info("使用一账号给停用邮箱功能的账号发送邮件")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入邮箱界面")
        Common.touch_text_by_class_name(self, ClassName.center, "邮箱", "p")

        logger.info("向已禁用邮箱的账号发送邮件")
        Mail.send_mail(self, Content.register_count, mail_theme="mail_theme")

        logger.info("切换至管理端启用邮箱")
        Common.switch_window_handle(self, Common.get_window_handle(self)[0])
        Mail.open_or_close_mail_by_phone(self, Content.register_count, True)

        logger.info("切换至该账号，查看邮件是否收取正常")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入邮箱界面")
        Common.touch_text_by_class_name(self, ClassName.center, "邮箱", "p")

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
                i = i + 1
            res = False
        self.assertTrue(res)

        logger.info("查看是否收到邮件")
        theme_list = Common.get_text_by_class_name(self, ClassName.td_content_sp, "span")
        self.assertTrue(Common.check_text_in_list(self, theme_list, "mail_theme"))


 
     
