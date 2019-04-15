#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
approval_name = "sprint5_002"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE NAME = '%s'" % approval_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""创建相同名称的分组"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.wait(self, 2)

        logger.info("新建分组")
        Common.creat_new_group(self, approval_name)

        logger.info("判断是否可以创建成功")



    
