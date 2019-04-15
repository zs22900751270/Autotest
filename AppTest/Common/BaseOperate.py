#!/usr/bin/env python
# _*_coding:utf-8_*_

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AppTest.TestRunner import *
from AppTest.Common.Content import *
# from AppTest.Driver.Phone_Driver import *
from AppTest.Common.Ldap import *

'''
一些基础操作：滑动、截图、点击页面元素等
'''


class BaseOperate:
    def __init__(self, driver, sn):
        self.driver = driver
        self.sn = sn

    def shell(self, commend):
        """
        adb shell 命令
        :return:
        """
        os.system("adb shell %s" % commend)

    def operate_sql(self, sql, database):
        """
        通过命令操作数据库
        :param sql:
        :return:
        """
        db = pymysql.connect("114.116.46.120", "root", "Hqd@1234", database, charset="utf8")
        try:
            cur = db.cursor()
            cur.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()

    def get_info_by_sql(self, sql, database):
        """
        通过命令获取数据库信息
        :param sql:
        :return:
        """
        db = pymysql.connect("114.116.46.120", "root", "Hqd@1234", database, charset="utf8")
        try:
            cur = db.cursor()
            cur.execute(sql)
            db.commit()
            return cur.fetchall()[0][0]
        except:
            db.rollback()
        db.close()

    def del_friend_by_sql(self, user_phone, friend_phone):
        """
        delete friend relationship by sql
        :return:
        """
        sql1 = "select id from user where phone='%s'" % user_phone
        user_id1 = BaseOperate.get_info_by_sql(self, sql1, "scap")
        sql2 = "select id from user where phone='%s'" % friend_phone
        user_id2 = BaseOperate.get_info_by_sql(self, sql2, "scap")
        del_sql1 = "delete from friend where user_id='%s' and friend_id='%s'" % (user_id1, user_id2)
        del_sql2 = "delete from friend where user_id='%s' and friend_id='%s'" % (user_id2, user_id1)
        BaseOperate.operate_sql(self, del_sql1, "scap")
        BaseOperate.operate_sql(self, del_sql2, "scap")

    def modify_user_info_by_sql(self, type, value, phone):
        """"""
        sql = "UPDATE scap.user SET %s='%s' WHERE phone='%s'" % (type, value, phone)
        BaseOperate.operate_sql(self, sql, "scap")

    def del_friend_request_by_sql(self, phone):
        """
        delete friend request by sql , only delete info when statue=0
        :param phone:
        :return:
        """
        friend_id = BaseOperate.get_info_by_sql(self, "select id from scap.user where phone='%s'" % phone, "scap")
        BaseOperate.operate_sql(self, "delete from scap.request_friend where friend_id='%s'" % friend_id, "scap")

    def getprojectpath(self):
        projectpath = os.path.abspath(os.path.pardir)
        if "AppTest" in projectpath:
            self.projectpath = projectpath
        else:
            self.projectpath = projectpath + "\\AppTest"
        if "testCase" in self.projectpath:
            self.projectpath = self.projectpath[:-(len("testCase")+1)]
        return self.projectpath

    def get_window_size(self):
        """
        获取屏幕大小
        :return: windowsize
        """
        global windowSize
        windowSize = self.driver.get_window_size()
        return windowSize

    def swipe(self, direction, times=1):
        """
        上下左右滑动，根据direction确定
        :return:
        """
        windowsSize = self.driver.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        diretion_list = {
            "right": [1 / 7, 1 / 2, 6 / 7, 1 / 2],
            "left": [6 / 7, 1 / 2, 6 / 7, 1 / 2],
            "up": [1 / 2, 6 / 7, 1 / 2, 1 / 7],
            "down": [1 / 2, 1 / 7, 1 / 2, 6 / 7]
        }

        for i in range(times):
            self.driver.swipe(diretion_list[direction][0] * width, diretion_list[direction][1] * height,
                              diretion_list[direction][2] * width, diretion_list[direction][3] * height, 200)

    def checkIfTextExist(self, text, scroll=True):
        """
        在当前界面内查找文字
        :param text: 所查找的文字
        :param scroll: 是否滑动查找
        :return:
        """
        try:
            if scroll:
                self.driver.find_element_by_android_uiautomator(
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "'
                    + text + '")')
            else:
                self.driver.find_element_by_name(text)
            logger.info("%s存在于界面中" % text)
            return True
        except:
            logger.info("%s不存在于界面中" % text)
            return False

    def checkIfIdExist(self, id):
        """
        通过Id点击控件
        :return:
        """
        try:
            aa = self.driver.find_elements_by_id(id)
            if len(aa) == 0:
                logger.info("%s不存在于当前界面" % id)
                return False
            else:
                logger.info("%s存在于当前界面" % id)
                return True
        except:
            logger.info("方法运行出错")
            return False

    def touchById(self, id, long=False, t=2):
        """
        通过Id点击控件
        :return:
        '"""
        clickAction = self.driver.find_element_by_id(id)
        if long:
            action = TouchAction(self.driver)
            action \
                .long_press(clickAction) \
                .release()
            action.perform()
            return self
        else:
            clickAction.click()

    def touch_id_by_index(self, id, index=1, t=2):
        """
        touch id by index
        :param id:
        :param index:
        :return:
        """
        ele_list = BaseOperate.get_results_by_id(self, id)
        BaseOperate.touch_by_element(self, ele_list[index-1], t=t)
        BaseOperate.wait(self, t)

    def touch_id_by_element(self, element, id):
        """
        touch id by element
        :param element:
        :param id:
        :return:
        """
        ele = element.find_element_by_id(id)
        ele.click()

    def touchByText(self, text):
        """
        通过文本点击控件
        :return:
        """
        clickAction = self.driver.find_element_by_android_uiautomator('text(\"'+text+'\")')
        clickAction.click()

    def sendTextById(self, id, text, clear=True):
        """
        在对应的id中输入相应的文字
        clear:是否清除原有文字
        :return:
        """
        inputText = self.driver.find_element_by_id(id)
        if clear:
            inputText.click()
            inputText.clear()
        inputText.send_keys(text)
        BaseOperate.go_back(self)

    def send_text_by_ele(self, ele, text, clear=True):
        """
        在对应的id中输入相应的文字
        clear:是否清除原有文字
        :return:
        """
        if clear:
            ele.click()
            ele.clear()
        ele.send_keys(text)
        BaseOperate.hide_keyboard(self)

    def openOrCloseSwitch(self, id=id, expect=True):
        """
        打开或关闭手机switch开关
        :param id:开关id
        :param expect:预期结果，打开或关闭
        :return:
        """
        switchBotton = self.driver.find_element_by_id(id)
        value = switchBotton.get_attribute("checked")
        if value == "false" and expect:
            switchBotton.click()
        elif value == "true" and not expect:
            switchBotton.click()
        else:
            logger.info("开关的预期结果和实际结果相同")
            pass

    def click_by_coordinate(self, x, y):
        """
        click by coordinate
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        action = TouchAction(self.driver)
        action \
            .press(None, x, y) \
            .release()
        action.perform()
        return self

    def startActivity(self, package, activity, t=10):
        """
        start activity
        :param package: package name
        :param Activity: activity name
        :return:
        """
        self.driver.start_activity(package, activity)
        BaseOperate.wait(self, t)
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_deny_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_deny_button)
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_btn_selectNegative):
            text = BaseOperate.get_text_by_id(self, PhoneControl.id_btn_selectNegative)
            if "取消" in text:
                BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_selectNegative)

    def get_frist_app_name(self):
        """
        获取第一个已启用的app名称
        :return:
        """
        app_name = BaseOperate.get_info_by_sql(self, "select name from app_entity", "application_center")
        BaseOperate.operate_sql(self,
                                "update application_center.app_entity set run_state='1' where name = '%s'" % app_name,
                                "application_center")
        return app_name

    def wait(self, t):
        """
        休眠t秒
        :param t: 休眠时间
        :return:
        """
        time.sleep(t)

    def get_identifying_code(self, phonenum):
        """get identifying code"""
        BaseOperate.wait(self, 5)
        redisIP = '114.116.46.120'
        Redis_port = 5079
        pool = redis.ConnectionPool(host=redisIP, port=Redis_port)
        conn_redis = redis.Redis(connection_pool=pool)
        for i in range(0, 4):
            params = conn_redis.get("app:user:verifyCode:%s:%s" % (phonenum, i))
            if params is not None:
                para = params
                break
        a = str(para)[-8:-2]
        logger.info("identify code:"+a)
        return a

    def get_captchaCode_code(self, phonenum):
        """get identifying code"""
        BaseOperate.wait(self, 5)
        redisIP = '114.116.46.120'
        Redis_port = 5079
        pool = redis.ConnectionPool(host=redisIP, port=Redis_port)
        conn_redis = redis.Redis(connection_pool=pool)
        params = conn_redis.get("app:user:captchaCode:%s" % phonenum)
        logger.info(params)
        a = str(params)[-6:-2]
        logger.info("captcha code:"+a)
        return a

    def find_toast(self, toast_text):
        """查找toast"""
        try:
            message = '//*[@text=\'{}\']'.format(toast_text)
            element = WebDriverWait(self.driver, 10, 0.1).until(
                EC.presence_of_element_located((By.XPATH, message)))
            logger.info("获取到的Toast:"+element.text)
            if element.text == toast_text:
                logger.info("查找Toast成功")
                logger.info(element.text)
                return True
            else:
                logger.info("查找Toast失败")
                return False
        except:
            logger.info("方法运行失败")
            return False

    def installApp(self, Apkname):
        """
        install apk
        :param Apkname: apk name
        :return:
        """
        apkpath = project_path + "/resource/Apk/"
        logger.info(apkpath)
        os.popen("adb install -r %s" % apkpath + Apkname)
        BaseOperate.wait(self, 5)
        logger.info("继续")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_button1)
        BaseOperate.wait(self, 6)
        logger.info("继续2")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_ok_button)
        logger.info("继续3")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_done_button)
        BaseOperate.wait(self, 5)

    def inithqdApp(self):
        """

        init phone afer install app
        :return:
        """
        # self.driver.start_activity("com.hqd.app_manager", "com.hqd.app_manager.feature.SplashActivity")
        # time.sleep(5)
        # self.driver.find_element_by_id("com.hqd.app_manager:id/meLayout").click()
        # self.driver.find_element_by_id("com.hqd.app_manager:id/shezhi").click()
        # self.driver.swipe(50, 1000, 50, 50, 200)
        # self.driver.find_element_by_id("com.hqd.app_manager:id/edit_ip").send_keys("https://114.116.46.120")
        # self.driver.find_element_by_id("com.hqd.app_manager:id/save_btn").click()
        # self.driver.close_app()
        pass

    def report_screen_shot(self, case_name):
        """"""
        try:
            config = configparser.ConfigParser()
            config.read("config.ini")
            srceen_shot_path = config.get("screenShot", "screenshot_folder_name")
            screen_shot_name = case_name[:-3] + ".png"
            self.driver.get_screenshot_as_file(srceen_shot_path + "/" + screen_shot_name)
        except:
            logger.info("截图失败或者单独运行时不截图")
        logger.info("-------------------%s test finish------------------" % case_name)

    def uninstallApp(self, package):
        """
        uninstall apk
        :param package: package name
        :return:
        """
        os.popen("adb uninstall %s" % package)

    def layout(self):
        """
        layout
        :return:
        """
        self.driver.back()
        self.driver.back()
        self.driver.find_element_by_id("com.hqd.app_manager:id/meLayout").click()
        self.driver.find_element_by_id("com.hqd.app_manager:id/shezhi").click()
        self.driver.find_element_by_id("com.hqd.app_manager:id/log_out").click()

    def get_text_by_id(self, id):
        """
        get text by id
        :param id: id
        :return:
        """
        text = self.driver.find_element_by_id(id).text
        return text

    def get_text_list_by_id(self, id):
        """
        get text_list by id
        :param id: id
        :return: ---> <list>
        """
        name_ele = BaseOperate.get_results_by_id(self, id)
        name_list = BaseOperate.get_text_list_by_ele(self, name_ele)
        return name_list

    def get_result_by_id(self, id):
        """
        get text by id
        :param id: id
        :return:
        """
        ele_list = self.driver.find_element_by_id(id)
        return ele_list

    def get_results_by_id(self, id):
        """
        get text by id
        :param id: id
        :return:
        """
        ele_list = self.driver.find_elements_by_id(id)
        return ele_list

    def clear_text_by_id(self, id):
        """
        clear text by id
        :param id: element id
        :return:
        """
        self.driver.find_element_by_id(id).clear()

    def go_back(self):
        """
        return parent page
        :return:
        """
        self.driver.back()

    def go_home(self):
        """
        return home page
        :return:
        """
        os.popen("adb shell input keyevent 3")

    def get_parameter_by_id(self, id, parameter):
        """
        get parameter by id
        :param id: id
        :param parameter: parameter
        :return:
        """
        element = self.driver.find_element_by_id(id)
        new_parameter = element.get_attribute(parameter)
        return new_parameter

    def clear_group_by_user(self, phone_num):
        """"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.group WHERE creator='%s'" % id, "scap")

    def input_text_by_cmd(self, text):
        """
        input text by cmd
        :param text: text
        :return:
        """
        os.popen("adb shell input text %s" % text)

    def touch_by_class_name(self, class_name):
        """
        touch by class name
        :return:
        """
        self.driver.find_element_by_class_name(class_name).click()

    def get_text_by_class_name(self, class_name):
        """
        get texts by class_name
        :return:
        """
        try:
            class_name_text = []
            elements = self.driver.find_elements_by_class_name(class_name)
            for i in elements:
                class_name_text.append(i.text)
            logger.info("通过class_name获取Text成功")
            return class_name_text
        except:
            logger.info("通过class_name获取Text失败")

    def get_result_by_class_name(self, class_name):
        """
        get result by class name
        :param class_name:
        :return:
        """
        return self.driver.find_element_by_class_name(class_name)

    def get_results_by_class_name(self, class_name):
        """
        get result by class name
        :param class_name:
        :return:
        """
        return self.driver.find_elements_by_class_name(class_name)

    @staticmethod
    def check_text_in_list(self, list, text):
        """
        在list中的某一项是否包含text
        :param list:
        :param text:
        :return:
        """
        try:
            for con in list:
                if text in con:
                    logger.info("text包含在list元素中")
                    return True
            logger.info("text未包含在list元素中")
            return False
        except:
            logger.info("text未包含在list元素中")

    @staticmethod
    def touch_by_element(self, element, t=2):
        """
        touch element by class_element
        :param element:
        :return:
        """
        element.click()
        time.sleep(t)

    @staticmethod
    def touch_text_by_elements(self, elements, text):
        """
        touch text by elements
        :param elements: elements <list>
        :param text:
        :return:
        """
        try:
            ele_text = []
            for ele_content in elements:
                ele_text.append(ele_content.text)
            num = ele_text.index(text)
            elements[num].click()
            logger.info("通过elements点击%s成功" % text)
        except:
            logger.info("通过elements点击%s失败" % text)

    def touch_text_by_class_name(self, class_name, click_text):
        """
        touch text by class name
        :param class_name: class name
        :param text: text
        :return:
        """
        try:
            class_name_result = self.driver.find_elements_by_class_name(class_name)
            for class_name_content in class_name_result:
                if click_text == class_name_content.text:
                    class_name_content.click()
                    break
            logger.info("通过class_name点击%s成功" % click_text)
            time.sleep(2)
        except:
            logger.info("通过class_name点击%s失败" % click_text)

    def modify_password_by_phone(self, phone_num, new_password):
        """"""
        sql = "UPDATE scap.user SET PASSWORD='%s' WHERE phone='%s'" % (new_password, phone_num)
        BaseOperate.operate_sql(self, sql, "scap")
        Ldap.modify_attribute_by_name(self, phone_num, "users", "userPassword", new_password)

    def modify_login_count_by_phone(self, old_count, new_count):
        """"""
        sql = "UPDATE scap.user SET phone='%s' WHERE phone='%s'" % (new_count, old_count)
        BaseOperate.operate_sql(self, sql, "scap")
        Ldap.modify_attribute_by_name(self, old_count, "users", "cn", new_count)
        Ldap.modify_attribute_by_name(self, old_count, "users", "phone", new_count)

    def app_login(self, login_count, login_password):
        """
        app_login
        :return:
        """
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.sendTextById(self, PhoneControl.login_count, login_count)
        BaseOperate.sendTextById(self, PhoneControl.login_password, login_password)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn)
        BaseOperate.wait(self, 3)

    def app_login_out(self):
        """
        app_login_out
        :return:
        """
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.wait(self, 5)
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_setting)
        BaseOperate.wait(self, 1)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_log_out)
        BaseOperate.wait(self, 3)

    def touch_text_by_id(self, text, id):
        """
        touch text by id
        :return:
        """
        ele_list = BaseOperate.get_results_by_id(self, id)
        for ele in ele_list:
            if ele.text == text:
                BaseOperate.touch_by_element(self, ele)
                break

    def check_friend_request_exist(self, friend_name, result=True):
        """
        friend name
        :return:
        """
        text_list = BaseOperate.get_results_by_id(self, PhoneControl.id_contact_layout)
        for text in text_list:
            name = BaseOperate.get_result_by_element(self, text, PhoneControl.id_contact_item_name)
            if friend_name in name.text:
                para = text
                break
        add_btn = BaseOperate.get_result_by_element(self, para, PhoneControl.id_add)
        refuse_btn = BaseOperate.get_result_by_element(self, para, PhoneControl.id_refuse)
        if add_btn is not None and refuse_btn is not None and result:
            return True
        elif not result and add_btn is None and refuse_btn is None:
            return False

    def except_friend_requset_or_not(self, friend_name, result=True):
        """
        friend name
        :return:
        """
        text_list = BaseOperate.get_results_by_id(self, PhoneControl.id_contact_item_name)
        add_list = BaseOperate.get_results_by_id(self, PhoneControl.id_add)
        refuse_list = BaseOperate.get_results_by_id(self, PhoneControl.id_refuse)
        for i in range(len(text_list)):
            logger.info(text_list[i].text)
            if friend_name in text_list[i].text:
                para = i
                break
        if result:
            BaseOperate.touch_by_element(self, add_list[para])
        else:
            BaseOperate.touch_by_element(self, refuse_list[para])
        BaseOperate.wait(self, 2)

    def check_add_friend_result(self, friend_name, result=True):
        """
        check add friend result
        :param friend:
        :param result:
        :return:
        """
        text_list = BaseOperate.get_results_by_id(self, PhoneControl.id_contact_layout)
        for text in text_list:
            name = BaseOperate.get_result_by_element(self, text, PhoneControl.id_contact_item_name)
            if friend_name in name.text:
                para = text
                break
        ele = BaseOperate.get_result_by_element(self, para, PhoneControl.id_result)
        add_result = BaseOperate.get_text_by_ele(self, ele)
        if result and add_result == "已同意":
            return True
        elif not result and add_result == "已拒绝":
            return True
        else:
            return False

    def get_text_list_by_ele(self, eles):
        """
        get text list by ele
        :param eles:
        :return: list
        """
        text_list = []
        for ele in eles:
            text_list.append(ele.text)
        return text_list

    def get_text_by_ele(self, ele):
        """
        get text by ele
        :param ele:
        :return: str
        """
        return ele.text

    def get_realname_by_phone(self, phone_num):
        """
        get realname by phone
        :param phone_num:
        :return: str
        """
        friend_name = BaseOperate.get_info_by_sql(self,
                                                  "select realname from user where phone='%s'" % phone_num,
                                                  "scap")
        return friend_name

    def creat_friend_by_sql(self, user_phone, friend_phone):
        """
        delete friend relationship by sql
        :return:
        """
        now, end = BaseOperate.get_start_and_end_time(self)
        sql1 = "select id from user where phone='%s'" % user_phone
        user_id1 = BaseOperate.get_info_by_sql(self, sql1, "scap")
        sql2 = "select id from user where phone='%s'" % friend_phone
        user_id2 = BaseOperate.get_info_by_sql(self, sql2, "scap")
        creat_sql1 = "INSERT INTO scap.friend(user_id, friend_id, create_time, update_time) VALUES('%s', '%s', '%s', '%s')"\
                   % (user_id1, user_id2, now, now)
        creat_sql2 = "INSERT INTO scap.friend(user_id, friend_id, create_time, update_time) VALUES('%s', '%s', '%s', '%s')" \
                   % (user_id2, user_id1, now, now)
        BaseOperate.operate_sql(self, creat_sql1, "scap")
        BaseOperate.operate_sql(self, creat_sql2, "scap")

    def creat_mission(self, mission_name, bz=None):
        """"""
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 1)
        BaseOperate.sendTextById(self, PhoneControl.id_content, mission_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_executor_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_self_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_start_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        if bz is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_remark, bz)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

    def delete_mission_record_by_sql(self, phone_num):
        """"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.task WHERE creator='%s' OR executor='%s'" % (id, id), "scap")

    def get_result_by_element(self, ele, id):
        """
        get result by element
        :param ele:
        :param id:
        :return:
        """
        element = ele.find_element_by_id(id)
        return element

    def creat_schedule(self, sechdule, bz=None, remind=None):
        """"""
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 3)
        BaseOperate.sendTextById(self, PhoneControl.id_content, sechdule)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_start_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_end_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btnSubmit)
        if remind is not None:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_again_layout)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, remind)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_left_btn)
        if bz is not None:
            BaseOperate.sendTextById(self, PhoneControl.id_remark, bz)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

    def creat_meeting(self, meeting_theme, meeting_content, meeting_area, remind=None):
        """"""
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_rfab__content_label_list_label_tv, 2)
        BaseOperate.sendTextById(self, PhoneControl.id_theme, meeting_theme)
        BaseOperate.sendTextById(self, PhoneControl.id_content, meeting_content)
        BaseOperate.hide_keyboard(self)
        BaseOperate.sendTextById(self, PhoneControl.id_locate, meeting_area)
        BaseOperate.hide_keyboard(self)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_take_in_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_contact_layout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)
        if remind is not None:
            BaseOperate.touch_id_by_index(self, PhoneControl.id_content)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, remind)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

    def delete_meeting_record(self, count_phone):
        """
        delete meeting record
        :param meeting_name:
        :param count_phone:
        :return:
        """
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.conference WHERE creator='%s'" % id, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.participant WHERE participant_id = '%s'" % id, "scap")

    def delete_schedule_record(self, count_phone):
        """
        delete meeting record
        :param meeting_name:
        :param count_phone:
        :return:
        """
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        BaseOperate.operate_sql(self, "delete from scap.schedule WHERE creator='%s'" % id, "scap")

    def modify_meeting_time(self, start_time, end_time, theme, creator):
        """modify meeting time by sql"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % creator, "scap")
        sql = "UPDATE scap.conference SET start_time = '%s' , end_time = '%s' WHERE theme = '%s' AND creator = '%s'" % (start_time, end_time, theme, id)
        BaseOperate.operate_sql(self, sql, "scap")

    def modify_sechdule_time(self, start_time, end_time, content, creator):
        """modify sechdule time by sql"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % creator, "scap")
        sql = "UPDATE scap.schedule SET start = '%s' , end = '%s' WHERE content = '%s' AND creator = '%s'" % (start_time, end_time, content, id)
        BaseOperate.operate_sql(self, sql, "scap")

    def get_start_and_end_time(self, type="minute", time_len=5):
        """"""
        now = datetime.datetime.now()
        if type == "hour":
            format_time = now + datetime.timedelta(hours=time_len)
        elif type == "minute":
            format_time = now + datetime.timedelta(minutes=time_len)
        elif type is None:
            format_time = now
        start_time = datetime.datetime.strftime(format_time, "%Y-%m-%d %H:%M:%S")
        end_time = format_time + datetime.timedelta(hours=1)
        end_time = datetime.datetime.strftime(end_time, "%Y-%m-%d %H:%M:%S")
        return start_time, end_time

    def clear_opened_app(self, phone):
        """"""
        user_id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone,
                                              "scap")
        BaseOperate.operate_sql(self,
                                "DELETE FROM application_center.app_entity_user WHERE user_id='%s'" % user_id,
                                "application_center")

    def creat_file_in_android(self, file_name, folder_name, input=None):
        """
        size 单位为Byte
        :param file_name:
        :param size:
        :return:
        """
        folder_path = Content.cloud_path + folder_name
        BaseOperate.shell(self, "mkdir %s" % folder_path)
        if input is None:
            BaseOperate.shell(self, "touch %s/%s" % (folder_path, file_name))
        if input is not None:
            if not os.path.exists(project_path + "/resource/cloud_upload_file"):
                os.mkdir(project_path + "/resource/cloud_upload_file")
            upload_file_path = project_path + "/resource/cloud_upload_file/" + file_name
            with open(upload_file_path, "w") as f:
                f.write(input)
            cmd = "adb push %s %s" % (upload_file_path, folder_path)
            os.system(cmd)

    def creat_file_from_window_to_android(self, file_name, folder_name, size=100):
        """
        size 单位为Byte
        :param file_name:
        :param size:
        :return:
        """
        if not os.path.exists(project_path + "/resource/cloud_upload_file"):
            os.mkdir(project_path + "/resource/cloud_upload_file")
        upload_file_path = project_path + "/resource/cloud_upload_file/" + file_name
        os.system("fsutil file createnew %s %s" % (upload_file_path, size))
        folder_path = Content.cloud_path + folder_name
        BaseOperate.shell(self, "mkdir %s" % folder_path)
        cmd = "adb push %s %s" % (upload_file_path, folder_path)
        os.system(cmd)

    def del_cloud_file_by_user(self, count_phone):
        """"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.disk_user_file WHERE user_id='%s'" % id, "scap")
        BaseOperate.operate_sql(self, "UPDATE scap.`disk_user_manage` SET used_size ='0' WHERE user_id='%s'" % id, "scap")

    def del_dept_cloud_file_by_user_and_file(self, count_phone, file_name):
        """"""
        id = BaseOperate.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        sql = "SELECT dept_id FROM scap.`disk_dept_file` WHERE user_id = '%s' AND NAME='%s'" % (id, file_name)
        dept_id = BaseOperate.get_info_by_sql(self, sql, "scap")
        BaseOperate.operate_sql(self, "DELETE FROM scap.`disk_dept_file` WHERE dept_id ='%s'" % dept_id,
                                "scap")
        BaseOperate.operate_sql(self, "UPDATE scap.`disk_dept_manage` SET used_size = '0' WHERE dept_id='%s'" % dept_id,
                                "scap")

    def clear_android_local_file(self, folder_name):
        try:
            folder_path = Content.cloud_path + folder_name
            BaseOperate.shell(self, "rm -r " + folder_path)
            logger.info("删除文件成功")
        except:
            logger.info("删除文件失败")

    def clear_window_local_file(self):
        try:
            if os.path.exists(project_path + "/resource/cloud_upload_file"):
                shutil.rmtree(project_path + "/resource/cloud_upload_file")
        except:
            logger.info("删除文件失败")

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            logger.info("隐藏键盘成功")
        except:
            logger.info("隐藏键盘失败")

    def check_protocol(self, phone_num):
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_button)
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phone_num)
        BaseOperate.touch_id_by_index(self, PhoneControl.register_verify_button)
        get_ident_phone = BaseOperate.get_identifying_code(self, phone_num)
        BaseOperate.sendTextById(self, PhoneControl.id_verify_code_edit, get_ident_phone)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_next_btn)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_user_agreement_text)

    def touch_more_by_name_in_cloud(self, name):
        """"""
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        for i in range(len(name_list)):
            if name == name_list[i]:
                BaseOperate.touch_id_by_index(self, PhoneControl.id_oper, i+1)

    def touch_search_by_id(self, id):
        """
        鼠标定位在id所属的input框，且输入法为搜狗输入法时才可使用
        touch search by id
        :param id:
        :return:
        """
        BaseOperate.touch_id_by_index(self, id)
        self.driver.keyevent("66")
    
    def quit(self):
        """
        first
        :return:
        """
        self.driver.quit()
