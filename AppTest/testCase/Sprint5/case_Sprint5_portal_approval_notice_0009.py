#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "zhangsen_title"
content = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssss"


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
        Common.connect_sql(self, "delete from sys_message where title='%s'" % title, "scap")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("点击发布事件")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "发布事件", "button")

        logger.info("编辑发布的事件")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "标题", title)
        con = Common.get_result_by_class_name_blank(self, "div", ClassName.qleditor_blank)
        Common.send_text_by_element(self, con, "标题", title)

        logger.info("选择分类")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "系统公告")
        Common.touch_text_by_class_name(self, ClassName.ivu_radio_wrapper_group_item, "系统公告", "label")

        logger.info("点击发送")
        Common.touch_text_by_class_name(self, ClassName.ivu_reload_success, "发送", "button")

        logger.info("撤回公告消息")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "所有")
        Common.touch_class_name_by_name(self, title, "button", ClassName.ivu_btn_error_small)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断是否撤回成功")
        ele_list = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        text_list = Common.get_text_by_elements(self, ele_list)
        result = Common.check_text_in_list(self, text_list, title)
        self.assertFalse(result)



    
