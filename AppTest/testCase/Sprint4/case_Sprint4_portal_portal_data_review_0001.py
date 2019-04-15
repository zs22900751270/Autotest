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
        Common.connect_sql(self, "delete from isv_table where name='data_table_cn'", "scap")
        Common.quit(self)

    def test_step(self):
        u"""数据表管理页面添加数据表"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据审核管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据表管理")
        Common.wait(self, 3)

        logger.info("点击添加数据表")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加数据表", "button")

        logger.info("输入新的数据表参数")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择ISV服务商")
        res = Common.get_results_by_class_name_blank(self, "li", ClassName.ivu_select_item)[0]
        Common.touch_by_element(self, res)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据表名称", "data_table_cn")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据表英文名称", "sql_tabla_en")

        logger.info("输入新的数据项")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加数据项", "button")

        logger.info("输入数据项参数")
        info_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.ivu_table_body)
        info_input = Common.get_class_name_elements_by_element_blank(self, info_ele, "input", ClassName.ivu_input)
        logger.info(len(info_input))
        for i in range(len(info_input)):
            Common.send_text_by_element(self, info_input[i], "data_para%s" % i)

        logger.info("点击保存数据表")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "保存数据表", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断数据是否创建成功")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_table_row, "tr")

        logger.info("检测是否创建成功")
        com_res = Common.check_text_in_list(self, text_list, "data_table_cn")
        self.assertTrue(com_res)



    
