#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
template_name = "template"


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
        Common.connect_sql(self, "delete from scap.report_template where tpl_name='%s'" % template_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""选择模板文件"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        if Common.get_display_status_by_text(self, "大数据展示"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "模版上传")

        logger.info("输入名称")
        input_ele = Common.get_result_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_ele, template_name)

        logger.info("点击上传文件")
        Common.upload_file(self, ClassName.ivu_upload_input, "html", "test_htm.html")
        input_ele = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        Common.touch_by_element(self, input_ele[-1])

        logger.info("进行模板搜索")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入模板名称进行搜索", template_name)
        search_button = Common.get_result_by_class_name_blank(self, "i", ClassName.search_icon)
        Common.touch_by_element(self, search_button)

        logger.info("判断模板创建是成功")
        get_text_by_class_name = Common.get_text_by_class_name(self, ClassName.ivu_table_row)
        self.assertTrue(len(get_text_by_class_name) == 1)


