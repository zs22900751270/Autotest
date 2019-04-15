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
        Cloud.modify_cloud_enable_status_by_user(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""启用云盘"""
        logger.info("打开服务端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击进入内置应用界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用", "li")

        logger.info("点击进入邮箱管理界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "云盘管理", "div")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "云盘管理", "li")

        logger.info("查看是否进入邮箱管理界面")
        text_list = Common.get_text_by_class_name(self, ClassName.menu_title)
        self.assertTrue(Common.check_text_in_list(self, text_list, "云盘管理"))

        logger.info("先停用云盘")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入用户名、手机号进行搜索",
                                                       Content.register_count+"\n")
        Cloud.open_or_close_cloud_by_phone(self, Content.register_count, False)

        logger.info("切换至客户端查看该账号云盘是否可用")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入云盘界面")
        Common.touch_text_by_class_name(self, ClassName.center, "云盘", "p")
        text_used = Common.get_text_by_class_name(self, ClassName.ivu_modal_content)
        self.assertTrue(Common.check_text_in_list(self, text_used, "云盘未启用，暂时不能使用该功能。"))
        Common.wait(self, 3)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        center_1 = Common.get_text_by_class_name(self, ClassName.center)
        self.assertTrue(Common.check_text_in_list(self, center_1, "云盘"))

        logger.info("切换至管理端启用云盘")
        Common.switch_window_handle(self, Common.get_window_handle(self)[0])
        Cloud.open_or_close_mail_by_phone(self, Content.register_count, True)

        logger.info("切换至客户端查看云盘是否可用")
        Common.switch_window_handle(self, Common.get_window_handle(self)[1])
        Common.touch_text_by_class_name(self, ClassName.center, "云盘", "p")

        logger.info("判断是否进入云盘详情界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "云盘"))


 
     
