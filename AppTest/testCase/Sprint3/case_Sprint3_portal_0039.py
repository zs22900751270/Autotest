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
        Common.del_app_entity_by_name(self, "%app_name%")
        Common.quit(self)

    def test_step(self):
        u"""应用列表查询支持模糊查询"""
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_result)

        logger.info("点击应用管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用管理", "li")

        logger.info("进入应用列表界面")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "应用管理", "span")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "应用列表", "span")

        logger.info("点击添加应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加应用", "button")

        logger.info("上传图片")
        Common.upload_file(self, ClassName.ivu_upload_input, "icon", "icon.jpg")

        logger.info("输入应用名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入应用名称", "app_name")

        logger.info("选择行业所属")
        Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_select_input, "请选择所属行业")
        result = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_form_item_required, "选择所属行业")
        item = Common.get_class_name_elements_by_element_blank(self, result, "li", ClassName.ivu_select_item)
        Common.touch_by_element(self, item[0])

        logger.info("选择付费方式-免费")
        Common.touch_text_by_class_name(self, ClassName.ivu_radio_wrapper_group_item, "免费开通", "label")

        logger.info("输入产品负责人")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入产品负责人", "zhangsen")

        logger.info("输入产品负责人联系方式")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入负责人联系方式", "12345678901")

        logger.info("选择应用开发商")
        Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_select_input, "请选择应用开发商")
        result = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_form_item_required, "应用开发商")
        item = Common.get_class_name_elements_by_element_blank(self, result, "li", ClassName.ivu_select_item)
        Common.touch_by_element(self, item[0])

        logger.info("输入应用连接")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入应用链接", "http://www.baidu.com")

        logger.info("输入应用连接详情")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入应用详情链接", "http://www.baidu.com")

        logger.info("点击保存")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "提交审核", "button")

        logger.info("通过搜索检测是否创建成功")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入应用名称、ISV名称进行搜索", "p_nam")
        Common.touch_search_by_placeholder(self, "输入应用名称、ISV名称进行搜索")
        search_result = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        self.assertEqual(len(search_result), 1)


