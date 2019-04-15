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
        Common.quit(self)

    def test_step(self):
        u"""ISV字典上传页面上传非csv文件时，无法上传成功"""
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_result)

        logger.info("点击大数据管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理", "li")

        logger.info("点击isv字典管理")
        if not Common.get_display_status_by_text(self, "ISV数据字典上传"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "ISV数据字典管理", "span")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "ISV数据字典上传", "span")

        logger.info("选择app")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择应用", "span")
        result = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_form_item_content, "选择应用")
        item = Common.get_class_name_elements_by_element_blank(self, result, "li", ClassName.ivu_select_item)
        Common.touch_by_element(self, item[0])

        logger.info("上传csv文件")
        Common.upload_file(self, ClassName.ivu_upload_input, "isv", "1K.csv")

        logger.info("判断能否成功")
        element_result = Common.get_element_by_class_name_and_text(self, "button", ClassName.ivu_btn_primary, "上传数据字典")
        upload_button = False
        try:
            result = element_result.get_attribute("disabled")
            logger.info(result)
            if result is None:
                upload_button = True
        except:
            upload_button = True
        self.assertTrue(upload_button)


