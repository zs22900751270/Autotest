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
        Cloud.del_cloud_file_by_user(self, Content.register_count)
        Cloud.clear_cloud_local_file(self)
        Common.quit(self)

    def test_step(self):
        u"""上传文件过程中关闭页面"""
        logger.info("打开客户端")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击进入云盘界面")
        Common.touch_by_id(self, ID.diskBtn)

        logger.info("查看是否进入云盘界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link)
        self.assertTrue(Common.check_text_in_list(self, text_list, "个人云盘"))

        logger.info("点击创建文件夹")
        Cloud.upload_file(self, "file_name_1", 10240000, 1)
        Common.close(self)

        logger.info("重新登录，查看是否上传成功")
        Common.switch_window_handle(self, Common.get_window_handle(self)[0])
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击进入云盘界面")
        Common.touch_by_id(self, ID.diskBtn)

        logger.info("查看是否进入云盘界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link)
        self.assertTrue(Common.check_text_in_list(self, text_list, "个人云盘"))

        logger.info("查看是否上传成功")
        file_name_list = Common.get_text_by_class_name(self, ClassName.rowName, "span")
        self.assertFalse(Common.check_text_in_list(self, file_name_list, "file_name_1"))



