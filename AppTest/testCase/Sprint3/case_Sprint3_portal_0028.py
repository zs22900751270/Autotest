#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
classify = "zhangsen"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.del_app_classify_by_name(self, classify)
        Common.quit(self)

    def test_step(self):
        u"""应用管理添加应用分类不能添加重复的分类"""
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_result)

        logger.info("点击应用管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用管理", "li")

        if Common.get_display_status_by_text(self, "行业分类", 1):
            logger.info("进入应用分类界面")
            Common.touch_text_by_class_name(self, ClassName.layout_text, "应用管理", "span")
            Common.touch_text_by_class_name(self, ClassName.layout_text, "行业分类", "span")

        logger.info("获取应用分类数量")
        for i in range(2):
            logger.info("点击添加分类,并输入参数，点击确定")
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加分类", "button")
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classify)
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input_number_input, "请输入分类排序",
                                                           1000)
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        result1 = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")[0]
        self.assertTrue("分类名称重复" in result1)



