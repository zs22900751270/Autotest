#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"


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
        BaseOperate.del_cloud_file_by_user(self, Content.register_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""文件夹删除"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, "zs_test")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("点击“...”")
        BaseOperate.touch_more_by_name_in_cloud(self, "zs_test")
        text_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_text)
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "重命名"))
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "移动"))
        self.assertTrue(BaseOperate.check_text_in_list(self, text_list, "删除"))

        logger.info("点击删除")
        BaseOperate.touch_text_by_id(self, "删除", PhoneControl.id_text)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)

        logger.info("查看是否删除成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertFalse(BaseOperate.check_text_in_list(self, name_list, "zs_test"))


 
     
