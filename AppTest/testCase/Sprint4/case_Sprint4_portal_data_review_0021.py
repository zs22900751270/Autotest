#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.quit(self)

    def test_step(self):
        u"""数据表管理页面添加数据表"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据审核管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据表管理")
        Common.wait(self, 3)

        logger.info("点击添加数据表")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择ISV服务商")
        result = Common.get_text_by_class_name(self, ClassName.ivu_select_item)
        self.assertTrue("深圳宏崎达信息工程有限公司" in result)



    
