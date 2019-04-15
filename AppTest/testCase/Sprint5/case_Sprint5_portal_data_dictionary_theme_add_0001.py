#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
long_theme_name = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
theme_name = "theme_add_01"


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
        Common.connect_sql(self, "DELETE FROM dict_theme WHERE NAME='%s'" % theme_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""删除审批流程"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.wait(self, 2)

        logger.info("点击标准数据字典管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "标准数据字典管理")
        Common.wait(self, 2)

        logger.info("点击数据字典主题")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据字典主题")
        Common.wait(self, 2)

        logger.info("点击添加主题，只输入一项，不能成功创建")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加主题", "button")

        logger.info("主题名称长度不能超过40")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入主题名称", long_theme_name)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        text_result = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        result1 = Common.check_text_in_list(self, text_result, "长度不能超过40字符")
        self.assertTrue(result1)

        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入主题名称", theme_name)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("创建失败")
        result2 = Common.check_text_in_list(self, text_result, "请选择分类")
        self.assertTrue(result2)



    
