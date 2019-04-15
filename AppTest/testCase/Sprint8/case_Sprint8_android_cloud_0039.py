#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


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
        u"""文件层级测试"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)

        logger.info("创建文件夹")
        for i in range(1, 16):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
            BaseOperate.sendTextById(self, PhoneControl.id_remark, "folder_%s" % i)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
            name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
            path_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_path_blue)
            self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "folder_%s" % i))
            self.assertEqual(len(name_list), 1)
            if i != 1:
                self.assertTrue(BaseOperate.check_text_in_list(self, path_list, "folder_%s" % (i-1)))
            if i != 15:
                BaseOperate.touch_text_by_id(self, "folder_%s" % i, PhoneControl.id_name)


 
     
