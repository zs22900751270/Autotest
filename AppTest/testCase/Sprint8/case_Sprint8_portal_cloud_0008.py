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
        Cloud.modify_cloud_enable_status_by_user(self, Content.register_count)
        Cloud.del_cloud_file_by_user(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""云盘运行一段时间停用云盘一段时间后再启用"""
        logger.info("打开服务端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入云盘界面")
        Common.touch_text_by_class_name(self, ClassName.center, "云盘", "p")

        logger.info("判断是否进入云盘详情界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "云盘"))

        logger.info("先上传一个文件")
        Cloud.upload_file(self, "cloud_file_1")

        logger.info("打开服务端停用云盘")
        Common.open_new_page_in_chrome(self, WebControlServer.web_url)
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
                                                       Content.register_count + "\n")
        Cloud.open_or_close_cloud_by_phone(self, Content.register_count, False)

        logger.info("然后启用云盘")
        Cloud.open_or_close_cloud_by_phone(self, Content.register_count, True)

        logger.info("重新进入云盘界面，查看之前上传文件是否缺失")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入云盘界面")
        Common.touch_text_by_class_name(self, ClassName.center, "云盘", "p")

        logger.info("判断是否进入云盘详情界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "云盘"))

        logger.info("查看文件是否存在")
        file_name_list = Common.get_text_by_class_name(self, ClassName.rowName, "span")
        self.assertTrue(Common.check_text_in_list(self, file_name_list, "cloud_file_1"))


 
     
