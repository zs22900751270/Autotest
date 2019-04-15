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
        logger.info("收尾工作")
        logger.info("删除已创建的审批")
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='%zhangsen%'", "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%approval_name%'", "scap")
        Common.quit(self)

    def test_step(self):
        u"""点击创建审批选择分组和审批名称不填写点击确定"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)

        logger.info("点击创建审批")
        creat_approval = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        Common.touch_by_element(self, creat_approval)

        logger.info("选择审批图标")
        approval_icon = Common.get_results_by_class_name(self, ClassName.iconitem)
        Common.touch_by_element(self, approval_icon[0])

        logger.info("选择分组与审批名称接不填，点击保存，保存失败")
        confirm_btn = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)[1]
        Common.touch_by_element(self, confirm_btn)
        get_error_text = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue("请选择分组" in get_error_text)
        self.assertTrue("请输入审批名称" in get_error_text)

        logger.info("选择分组与审批名称只选择一项，点击保存，保存失败")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择")
        select_item = Common.get_results_by_class_name(self, ClassName.ivu_select_item)
        Common.touch_by_element(self, select_item[0])
        confirm_btn = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)[1]
        Common.touch_by_element(self, confirm_btn)
        get_error_text = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(len(get_error_text) == 1)
        self.assertTrue("请输入审批名称" in get_error_text)

        logger.info("选择分组与审批名称两项都填写，点击保存，保存成功")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入审批名称", "approval_name")
        confirm_btn = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)[1]
        Common.touch_by_element(self, confirm_btn)

        logger.info("判断是否创建成功")
        created_approval = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        created_approval_name = Common.get_text_by_elements(self, created_approval)
        result = Common.check_text_in_list(self, created_approval_name, "approval_name")
        self.assertTrue(result)



    
