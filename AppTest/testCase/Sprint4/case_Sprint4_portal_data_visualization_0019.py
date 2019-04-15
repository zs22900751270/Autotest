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

        logger.info("未输入名称，且未上传文件，保存按钮无法点击")
        save_button = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        save_button_parm = save_button.get_attribute("disabled")
        self.assertEqual(save_button_parm, "true")

        logger.info("输入名称，且未上传文件，保存按钮无法点击")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入模版名称", template_name)
        save_button = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        save_button_parm = save_button.get_attribute("disabled")
        self.assertEqual(save_button_parm, "true")

        logger.info("未输入名称，已上传文件，保存按钮无法点击")
        Common.clear_text_by_class_name_and_placeholder(self, ClassName.ivu_input, "请输入模版名称")
        Common.upload_file(self, ClassName.ivu_upload_input, "html", "test_htm.html")
        save_button = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        save_button_parm = save_button.get_attribute("disabled")
        self.assertEqual(save_button_parm, "true")

        logger.info("输入名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入模版名称", template_name)

        logger.info("判断保存按钮是否可点")
        save_button = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        save_button_parm = save_button.get_attribute("disabled")
        self.assertIsNone(save_button_parm)



    
