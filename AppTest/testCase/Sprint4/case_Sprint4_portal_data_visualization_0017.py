#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
data_list_name = "data_list_1"
data_list_name_new = "data_list_new"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("清除新建的数据")

        Common.quit(self)

    def test_step(self):
        u"""数据集管理，删除数据库"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        if Common.get_display_status_by_text(self, "大数据展示"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "模版上传")

        logger.info("判断输入框是否有长度限制")
        ele_name = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)[0]
        get_attribute_result = ele_name.get_attribute("maxlength")
        self.assertTrue(get_attribute_result == "20")

        logger.info("判断输入框是否可为空")
        save_button = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)[0]
        get_disabled_result = save_button.get_attribute("disabled")
        self.assertTrue(get_disabled_result == "true")



    
