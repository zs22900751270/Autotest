#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""在通讯录界面搜索好友"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("清除好友信息")
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("创建好友关系")
        BaseOperate.creat_friend_by_sql(self, Content.register_count, Content.spare_count)
        friend_name = BaseOperate.get_realname_by_phone(self, Content.spare_count)

        logger.info("点击进行登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击搜索框，搜索已存在的好友")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_search)
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, friend_name)
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("判断搜索结果是否准确")
        name = BaseOperate.get_text_by_id(self, PhoneControl.id_contact_item_name_tv)
        self.assertEqual(name, friend_name)



    
