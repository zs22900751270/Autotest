#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
classify = "zhangsen"
classify_new = "senzhang"


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
        Common.del_app_classify_by_name(self, classify_new)
        Common.quit(self)

    def test_step(self):
        u"""数据标准字典编辑按钮正常编辑字典内容，点击取消后，重新打开编辑框，内容不变"""
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

        logger.info("点击添加分类,并输入参数，点击确定")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加分类", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classify)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input_number_input, "请输入分类排序",
                                                       "1000")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("通过搜索，确定修改成功")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入行业分类名称进行搜索", classify)
        search = Common.get_result_by_class_name_blank(self, "i", ClassName.search_icon)
        Common.touch_by_element(self, search)

        logger.info("判断是否创建成功")
        search_result = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        self.assertTrue(len(search_result) == 1)

        logger.info("进行编辑")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary_small, "编辑", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称", classify_new)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("通过搜索，确定修改成功")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入行业分类名称进行搜索", classify_new)
        Common.touch_search_by_placeholder(self, "输入行业分类名称进行搜索")

        logger.info("判断是否修改成功")
        search_result = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        self.assertTrue(len(search_result) == 1)



     
