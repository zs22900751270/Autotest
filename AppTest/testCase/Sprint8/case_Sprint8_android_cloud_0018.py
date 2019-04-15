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
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.clear_window_local_file(self)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""文件文件夹移动到文件夹时可以随时创建文件夹"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, "zs_test")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("点击“...”")
        BaseOperate.touch_more_by_name_in_cloud(self, "zs_test")

        logger.info("在移动过程中创建文件夹")
        BaseOperate.touch_text_by_id(self, "移动", PhoneControl.id_text)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, "test_zs")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否创建成功")
        BaseOperate.touch_text_by_id(self, "取消", PhoneControl.id_toolbar_right_tv)
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, "test_zs"))


 
     
