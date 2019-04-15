#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""日程编辑界面编辑日程提醒设置"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "服务")

        logger.info("点击任务")
        Common.touch_text_by_class_name(self, ClassName.center, "日程")

        logger.info("判断是否进入日程界面")
        text = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")[-1]
        self.assertEqual(text, "日程")

        logger.info("点击创建一个日程")
        Common.creat_schedule(self, "schedule_11")

        logger.info("点击编辑")
        Common.touch_del_or_edit_by_sechedule_name(self, "schedule_11")

        logger.info("判断是否进入编辑界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        res1 = Common.check_text_in_list(self, text_list, "编辑日程")
        self.assertTrue(res1)

        logger.info("修改日程提醒")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_selected_value, "不提醒", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "提前5分钟", "li")
        Common.touch_by_id(self, ID.submitAddScheduleBtn)

        logger.info("点击进入日程详情")
        ele = Common.get_element_by_class_name_and_text(self, "div", ClassName.schedule_item_name_ivu_col_span_14,
                                                        "schedule_11")
        Common.touch_tag_name_by_element(self, ele, "span")

        logger.info("判断是否修改成功")
        sechdule_list = Common.get_text_by_class_name(self, ClassName.item_content_ivu_col_span_18, "div")
        res1 = Common.check_text_in_list(self, sechdule_list, "提前5分钟")
        self.assertTrue(res1)


 
    
