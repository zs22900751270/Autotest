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
        logger.info("清除所创建的数据")
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
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据表名称", "data_table_cn")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据表英文名称", "sql_tabla_en")

        logger.info("创建数据项")
        Common.creat_data_item(self, 50)

        logger.info("点击保存数据表")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "保存数据表", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断数据是否创建成功")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_table_row, "tr")

        logger.info("检测是否创建成功")
        com_res = Common.check_text_in_list(self, text_list, "data_table_cn")
        self.assertTrue(com_res)

        logger.info("点击查看数据详情")
        Common.touch_class_name_by_name(self, "data_table_cn", "button", ClassName.ivu_btn_primary_small)
        info_ele = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_table_cell)
        self.assertEqual(len(info_ele)-3, 150)



    
