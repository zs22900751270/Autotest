#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name_90M = "zhangsen_90M"
file_name_11M = "zhangsen_11M"


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
        u"""当容量大于90M时上传11M的文件"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建两个大小为90M和11M的文件")
        BaseOperate.creat_file_from_window_to_android(self, file_name_90M, folder_name, 94371840)
        BaseOperate.creat_file_from_window_to_android(self, file_name_11M, folder_name, 11534336)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择大小为90M的文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name_90M)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)
        timeout = 0
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_btn_bubble) and timeout < 120:
            logger.info("上传中，请稍等。。。")
            BaseOperate.wait(self, 1)
            timeout = timeout + 1

        logger.info("上传完成，判断是否上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name_90M))

        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择大小为11M的文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name_11M)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook, t=0)

        logger.info("无法上传")
        self.assertTrue(BaseOperate.find_toast(self, "文件超过剩余空间大小，无法上传"))


 
     
