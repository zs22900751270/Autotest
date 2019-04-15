#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
group_name = "auto_test"
approval_name = "sprint5_17"


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
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='%s'" % group_name, "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%s'" % approval_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""审批修改"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)

        logger.info("点击创建分组")
        Common.creat_new_group(self, group_name)

        logger.info("点击创建审批")
        Common.creat_approval(self, group_name, approval_name)
        fin_result = Common.check_approval_in_group(self, approval_name, group_name)
        self.assertTrue(fin_result)

        logger.info("点击编辑分组")
        Common.wait(self, 3)
        edit_button = Common.touch_edit_by_group_name(self, group_name)
        logger.info("点击删除")
        del_button = Common.get_class_name_elements_by_element_blank(self, edit_button, "div", ClassName.edit_item)[1]
        Common.touch_by_element(self, del_button)
        get_text_content = Common.get_text_by_class_name(self, ClassName.ivu_modal_confirm_body)
        logger.info(get_text_content)
        result = Common.check_text_in_list(self, get_text_content, "分组下的审批将移动到【其他】中，确认要删除吗？")
        self.assertTrue(result)



    
