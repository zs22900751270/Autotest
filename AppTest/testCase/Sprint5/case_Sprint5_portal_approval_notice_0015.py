#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        Common.connect_sql(self, "delete from message_classify where name='%s'" % title, "scap")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("点击发布事件")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "发布事件", "button")

        logger.info("创建新的分类")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_info, "新建分类", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", title)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断是否创建成功")
        div_result = Common.get_result_by_class_name_blank(self, "div", ClassName.ivu_div_col_span_12)
        Common.touch_by_element(self, div_result)
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_select_dropdown_list, "ul")
        result = Common.check_text_in_list(self, text_list, title)
        self.assertTrue(result)



    
