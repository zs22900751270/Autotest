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
        Common.quit(self)

    def test_step(self):
        u"""文件显示更新日期和大小"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击进入云盘界面")
        Common.touch_by_id(self, ID.diskBtn)

        logger.info("查看是否进入云盘界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link)
        self.assertTrue(Common.check_text_in_list(self, text_list, "个人云盘"))

        logger.info("点击创建文件夹")
        Cloud.upload_file(self, "file_name_1")

        logger.info("查看是否创建创建成功，显示是否正常")
        self.assertTrue(Cloud.check_if_file_exist(self, "file_name_1"))

        logger.info("查看是否显示创建日期是否存在")
        upload_time = Cloud.get_upload_time_by_file_name(self, "file_name_1")
        upload_size = Cloud.get_upload_size_by_file_name(self, "file_name_1")
        self.assertIsNotNone(upload_time)
        self.assertEqual(upload_size, "1000.0KB")


 
     
