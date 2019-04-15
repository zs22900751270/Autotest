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
        u"""云盘搜索结果特别多"""
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
        for i in range(12):
            Cloud.upload_file(self, "folder_name_%s" % i)

        logger.info("搜索文件")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入文件名称", "folder_name_\n")

        logger.info("查看是否有分页")
        page_list = Common.get_text_by_class_name(self, ClassName.ivu_page_item)
        logger.info(page_list)
        self.assertTrue(Common.check_text_in_list(self, page_list, "2"))


 
     
