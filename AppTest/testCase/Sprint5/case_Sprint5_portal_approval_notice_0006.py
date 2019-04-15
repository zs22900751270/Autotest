#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
classification = "new_sen"
classification_new = "zhangsen"


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
        sql = "delete from message_classify where name like '%"+"%s" % classification+"%'"
        Common.connect_sql(self, sql, "scap")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        for i in range(1, 51):
            logger.info("第%s次创建分类" % i)
            Common.touch_text_by_class_name(self, ClassName.btn_addClass_btn, "新建分类", "button")
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分类名称",
                                                           classification+str(i))
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("50个分类显示正常")
        left_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.left)
        rename1 = Common.get_class_name_elements_by_element_blank(self, left_ele, "div", ClassName.group_edit)
        name_list = Common.get_text_by_elements(self, rename1)
        fin_result = True
        for j in range(1, 51):
            if Common.check_text_in_list(self, name_list, classification+str(i)):
                pass
            else:
                fin_result = False
        self.assertTrue(fin_result)



    
