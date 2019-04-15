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
        u"""点击创建审批审批名称输入超长"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)

        logger.info("点击创建审批")
        creat_approval = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        Common.touch_by_element(self, creat_approval)

        logger.info("判断输入长度是否符合标准")
        approval_name = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入审批名称")
        approval_dis = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入审批说明")
        len_approval_name = approval_name.get_attribute("maxlength")
        len_approval_dis = approval_dis.get_attribute("maxlength")
        self.assertEqual(len_approval_name, "20")
        self.assertEqual(len_approval_dis, "100")



    
