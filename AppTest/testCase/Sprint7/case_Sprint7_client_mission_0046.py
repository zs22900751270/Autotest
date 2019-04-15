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
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""新建任务"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("点击新建任务,指派给其他人")
        Common.touch_by_id(self, ID.createTask)
        choice = Common.get_result_by_class_name_blank(self, "i", ClassName.ivu_icon_plus_circled_icon_normal)
        Common.touch_by_element(self, choice)

        logger.info("获取好友名称")
        name_list = Common.get_text_by_class_name(self, ClassName.name, "span")
        name = list(filter(None, name_list))
        logger.info(name)

        logger.info("搜索该好友")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号或者姓名", name[0])

        logger.info("判断是否搜索成功")
        new_name_list = Common.get_text_by_class_name(self, ClassName.name, "span")
        new_name = list(filter(None, new_name_list))
        self.assertEqual(len(new_name), 1)


 
    
