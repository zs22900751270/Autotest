#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
sql_name = "zhangsen"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.connect_sql(self, "delete from report_database where name like '%zhangsen%'", "scap")
        Common.quit(self)

    def test_step(self):
        u"""数据集管理，删除数据库"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        if Common.get_display_status_by_text(self, "大数据展示"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据集管理")

        logger.info("点击添加数据库")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加数据库", "button")

        logger.info("输入参数, 输入错误的用户名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据源名称",
                                                       "zhangsen")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择数据库类型", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "mysql", "li")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据库地址",
                                                       "jdbc:mysql://114.116.46.120:3306/scap")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入用户名", "root")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "Hqd@1234")

        logger.info("点击保存，可以保存成功")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("选择所添加数据库")
        Common.touch_text_by_class_name(self, ClassName.ivu_checkbox_wrapper, "zhangsen", "label")

        logger.info("点击添加数据集数据")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入SQL脚本",
                                                       "select * from user")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入数据集名称",
                                                       "zsen_data_list")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_warning, "执行", "button")

        logger.info("判断是否执行成功")
        table_header = Common.get_text_by_class_name(self, ClassName.ivu_table_tip, "div")
        self.assertIsNotNone("暂无数据" not in table_header)



    
