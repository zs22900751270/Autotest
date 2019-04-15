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
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.quit(self)

    def test_step(self):
        u"""搜索好友不输入时点击搜索"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入通讯录界面")
        img = Common.get_results_by_class_name_blank(self, "div", ClassName.notice_toleft)[0]
        Common.touch_tag_name_by_element(self, img, "img", 1)

        logger.info("判断是否进入通讯录界面")
        text_list = Common.get_text_by_class_name(self, ClassName.guide, "h5")
        res = Common.check_text_in_list(self, text_list, "添加好友")
        self.assertTrue(res)

        logger.info("点击搜索之前获取所有好友姓名")
        sear = Common.get_text_by_class_name(self, ClassName.name, "span")

        logger.info("点击搜索")
        Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入姓名、电话搜索")
        Common.press_enter_in_window(self)

        logger.info("点击搜索之后获取所有好友姓名")
        new_sear = Common.get_text_by_class_name(self, ClassName.name, "span")

        logger.info("点击搜索按钮前后获取的好友姓名进行比较")
        self.assertEqual(sear, new_sear)


 
    
