#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
approval_name = "zhangsen"


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
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE NAME LIKE '%zhangsen%'", "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%approval_name%'", "scap")
        Common.quit(self)

    def test_step(self):
        u"""点击创建审批选择分组和审批名称不填写点击确定"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.wait(self, 2)

        logger.info("点击新建分组")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)
        aa = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_ghost)
        Common.touch_by_element(self, aa)

        logger.info("创建分组")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分组名称", "zhangsen")
        ok_but = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, ok_but)

        logger.info("点击创建审批")
        Common.creat_approval(self, "zhangsen", "approval_name")

        logger.info("创建应用成功")
        text_list = Common.get_text_by_class_name(self, ClassName.item_content_c, "div")
        result = Common.check_text_in_list(self, text_list, "approval_name")
        self.assertTrue(result)



    
