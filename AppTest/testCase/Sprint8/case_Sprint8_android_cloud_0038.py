#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name_90M = "zhangsen_90M"
file_name_9M = "zhangsen_9M"


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
        u"""已用和可用的云盘容量显示在云盘界面，上传或删除文件后随时发生变化"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建两个大小为90M和9M的文件")
        BaseOperate.creat_file_from_window_to_android(self, file_name_90M, folder_name, 94371840)
        BaseOperate.creat_file_from_window_to_android(self, file_name_9M, folder_name, 9437184)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        capacity_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_size).split("/")[0]
        self.assertEqual(capacity_1, "0KB")
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
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook, t=0)
        timeout = 0
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_btn_bubble) and timeout < 120:
            logger.info("上传中，请稍等。。。")
            BaseOperate.wait(self, 1)
            timeout = timeout + 1

        logger.info("上传完成，判断是否上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name_90M))

        logger.info("查看存量是否出现变化")
        BaseOperate.go_back(self)
        capacity_2 = BaseOperate.get_text_by_id(self, PhoneControl.id_size).split("/")[0]
        self.assertEqual(capacity_2, "90.0MB")

        logger.info("点击进入我的云盘界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择大小为9M的文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name_9M)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)
        timeout = 0
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_toolbar_right_btn_bubble) and timeout < 120:
            logger.info("上传中，请稍等。。。")
            BaseOperate.wait(self, 1)
            timeout = timeout + 1

        logger.info("上传完成，判断是否上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name_9M))

        logger.info("第二次查看存量是否出现变化")
        BaseOperate.go_back(self)
        capacity_3 = BaseOperate.get_text_by_id(self, PhoneControl.id_size).split("/")[0]
        self.assertEqual(capacity_3, "99.0MB")

        logger.info("删除90M文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_more_by_name_in_cloud(self, file_name_90M)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)

        logger.info("判断是否删除成功,空间大小是否变化")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertFalse(BaseOperate.check_text_in_list(self, name_list, file_name_90M))
        BaseOperate.go_back(self)
        capacity_4 = BaseOperate.get_text_by_id(self, PhoneControl.id_size).split("/")[0]
        self.assertEqual(capacity_4, "9.0MB")

        logger.info("删除9M文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)
        BaseOperate.touch_more_by_name_in_cloud(self, file_name_9M)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "删除")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectPositive)

        logger.info("判断是否删除成功,空间大小是否变化")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertFalse(BaseOperate.check_text_in_list(self, name_list, file_name_9M))
        BaseOperate.go_back(self)
        capacity_5 = BaseOperate.get_text_by_id(self, PhoneControl.id_size).split("/")[0]
        self.assertEqual(capacity_5, "0KB")


 
     
