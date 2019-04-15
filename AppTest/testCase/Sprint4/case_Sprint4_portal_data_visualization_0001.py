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
        u"""数据集管理，增加数据库"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        if Common.get_display_status_by_text(self, "数据集管理"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据集管理")
        logger.info("点击添加数据库")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加数据库", "button")

        logger.info("输入参数, 输入超长的数据源名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据源名称",
                                                       "zhangsenzhangsenzhangsenzhangsen")

        logger.info("点击保存，提示数据源名称不能超过20个字符")
        get_error_result = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue("长度不能超过20字符" in get_error_result)

        logger.info("输入参数, 输入错误的用户名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据源名称",
                                                       "zhangsen")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择数据库类型", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "mysql", "li")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据库地址",
                                                       "jdbc:mysql://114.116.46.120:3306/test")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入用户名", "toor")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "Hqd@1234")

        logger.info("点击保存，提示数据库配置异常")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        result1 = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")[0]
        self.assertTrue("数据库配置异常" in result1)
        Common.touch_text_by_class_name(self, ClassName.confirm, "OK")

        logger.info("输入参数, 输入错误的密码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入用户名", "root")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "Hqd@1234567")

        logger.info("点击保存，提示数据库配置异常")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        result1 = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")[0]
        self.assertTrue("数据库配置异常" in result1)



