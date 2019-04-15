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
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""未完成的页面查看我创建，我执行的任务详情"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)
        Common.wait(self, 2)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("创建一个任务")
        Common.creat_mission(self, "mission_content")

        logger.info("判断是否进入任务详情界面")
        Common.open_mission_detail_by_name(self, "mission_content", Content.register_count, 1)

        logger.info("判断左上角是否有编辑等按钮")
        self.assertTrue(Common.check_if_id_exist(self, ID.deteleTaskBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.editTaskBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.rewardTaskBtn))


 
    
