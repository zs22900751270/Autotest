#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Driver.Web_Driver import *
from AppTest.Common.Content import *
from pykeyboard import PyKeyboard
from AppTest.TestRunner import *
from selenium.webdriver.common.action_chains import ActionChains
keyboard = PyKeyboard()


class Common(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, web_driver):
        self.web_driver = web_driver
        # quit browser and end testing

    def connect_sql(self, sql, database):
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

    def get_all_info_by_sql(self, sql, database):
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
            return cur.fetchall()
        except:
            db.rollback()
        db.close()

    def quit_browser(self):
        self.web_driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.web_driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.web_driver.back()
        logger.info("Click back on current page.")

    # 点击关闭当前窗口
    def close(self):
        try:
            self.web_driver.close()
            logger.info("Closing and quit the browser.")
        except:
            logger.error("Failed to quit the browser with")

            # 保存图片

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = self.projectpath + "/report/screenshot/"
        logger.info(file_path)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.web_driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshot")
        except:
            logger.error("Failed to take screenshot!")
            self.get_windows_img()

    def switch_to_frame(self, frame):
        """
        tiao zhuan iframe kuang jia
        :param id:
        :return:
        """
        self.web_driver.switch_to_frame(frame)

    def scroll_page_top(self):
        """
        web scroll to top
        :return:
        """
        js = "var q=document.documentElement.scrollTop=0"
        # js = "window.scrollTo(0,0)"
        self.web_driver.execute_script(js)

    def scroll_page_end(self):
        """
        web scroll to top
        :return:
        """
        js = "var q=document.documentElement.scrollTop=1000000"
        # js = "window.scrollTo(0,document.body.scrollHeight)"
        self.web_driver.execute_script(js)

    def scroll_search_element(self, element):
        """
        hua dong cha zhao yuan su
        :return:
        """
        try:
            self.web_driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info("滑动查找元素成功")
        except:
            logger.info("滑动查找元素失败")
            return False

    def clear(self, xpath):
        el = self.web_driver.find_element_by_xpath(xpath)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except:
            logger.error("Failed to clear in input box")

    @staticmethod
    def move_mouse_on(self, element):
        """
        shu biao xuan ting
        :param element:
        :return:
        """
        ActionChains(self.web_driver).move_to_element(element).perform()

    @staticmethod
    def touch_by_xpath(self, xpath, t=2):
        element = self.web_driver.find_element_by_xpath(xpath)
        try:
            element.click()
            logger.info("success to click the element")
        except:
            logger.error("Failed to click the element")
        time.sleep(t)

    def get_page_title(self):
        logger.info("Current page title is %s" % self.web_driver.title)
        return self.web_driver.title

    @staticmethod
    def wait(self, t):
        time.sleep(t)

    def send_text_by_xpath(self, xpath, text, clear=True):
        """
        send text by id
        """
        element = self.web_driver.find_element_by_xpath(xpath)
        element.click()
        if clear:
            element.clear()
        element.send_keys(text)
        time.sleep(1)

    def get_text_by_xpath(self, xpath):
        """
        get text by xpath
        :return:
        """
        return self.web_driver.find_element_by_xpath(xpath).text

    def check_if_text_exist(self, xpath):
        """
        check_if_text_exist
        :return:
        """
        try:
            self.web_driver.find_element_by_link_text(xpath)
            logger.info("text存在")
            return True
        except:
            logger.info("text不存在")
            return False

    def get_identifying_code(self, phonenum):
        """get identifying code"""
        Common.wait(self, 5)
        redisIP = '114.116.46.120'
        Redis_port = 5079
        pool = redis.ConnectionPool(host=redisIP, port=Redis_port)
        conn_redis = redis.Redis(connection_pool=pool)
        for i in range(0, 4):
            params = conn_redis.get("app:user:verifyCode:%s:%s" % (phonenum, i))
            if params is not None:
                para = params
                break
        logger.info(para)
        a = str(para)[-8:-2]
        logger.info("identify code:"+a)
        return a

    def get_window_handle(self):
        """
        get window handle
        :return:
        """
        return self.web_driver.window_handles

    def switch_window_handle(self, window_ele):
        """
        switch window handle
        :return:
        """
        self.web_driver.switch_to_window(window_ele)

    def get_element_by_xpath(self, xpath):
        """
        get element by xpath
        :return:
        """
        return self.web_driver.find_element_by_xpath(xpath)

    def open_new_page_in_chrome(self, url, i=-1):
        """
        open a new page in chrome
        :param url: the page you want to open
        :return:
        """
        js = "window.open(\"%s\")" % url
        self.web_driver.execute_script(js)
        time.sleep(3)
        hands = Common.get_window_handle(self)
        Common.switch_window_handle(self, hands[i])
        Common.refresh(self, 5)


    @staticmethod
    def press_backspace_in_window(self, times=1):
        """
        get result by class name
        :param class_name:
        :return: type--><list>
        """
        for i in range(times):
            keyboard.tap_key(keyboard.backspace_key)

    def get_results_by_class_name(self, class_name):
        """
        get result by class name
        :param class_name:
        :return: type--><list>
        """
        return self.web_driver.find_elements_by_class_name(class_name)

    def get_result_by_class_name(self, class_name):
        """
        get result by class name
        :param class_name:
        :return:
        """
        return self.web_driver.find_element_by_class_name(class_name)

    def get_results_by_class_name_blank(self, tag_name, class_name):
        """
        use this method when "class name" has blank
        :param class_name:
        :return:
        """
        return self.web_driver.find_elements_by_css_selector("%s[class='%s']" % (tag_name, class_name))

    def get_result_by_class_name_blank(self, tag_name, class_name):
        """
        use this method when "class name" has blank
        :param class_name:
        :return:
        """
        return self.web_driver.find_element_by_css_selector("%s[class='%s']" % (tag_name, class_name))

    @staticmethod
    def touch_by_element(self, element, t=2):
        """
        touch element by class_element
        :param element:
        :return:
        """
        element.click()
        time.sleep(t)

    def get_class_name_elements_by_element(self, element_result, class_name):
        """
        get_class_name_element_by_element
        :param element_result:
        :return: type--><list>
        """
        return element_result.find_elements_by_class_name(class_name)

    @staticmethod
    def get_class_name_elements_by_element_blank(self, element_result, tag_name, class_name):
        """
        get_class_name_element_by_element
        :param element_result:
        :return: type--><list>
        """
        try:
            return element_result.find_elements_by_css_selector("%s[class='%s']" % (tag_name, class_name))
        except:
            logger.info("通过class_name获取不到元素")
            return False

    @staticmethod
    def get_text_by_elements(self, elements):
        """
        elements type--><list>
        :param elements:
        :return:
        """
        try:
            ele_text = []
            for ele_content in elements:
                ele_text.append(ele_content.text)
            return ele_text
        except:
            logger.info("获取text_list失败")
            return False

    @staticmethod
    def get_text_by_element(self, element):
        """
        elements type--><list>
        :param elements:
        :return:
        """
        return element.text

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
        Common.wait(self, 2)

    def get_text_by_class_name(self, class_name, tag_name=None):
        """
        get result by class name
        :param class_name:
        :return: type--><list>
        """
        try:
            class_name_text = []
            if tag_name is None:
                elements = self.web_driver.find_elements_by_class_name(class_name)
            else:
                elements = self.web_driver.find_elements_by_css_selector("%s[class='%s']" % (tag_name, class_name))
            for i in elements:
                class_name_text.append(i.text)
            logger.info("通过class_name获取Text成功")
            return class_name_text
        except:
            logger.info("通过class_name获取Text失败")

    def del_sql_list_by_name(self, name):
        """
        根据名称删除数据库内容
        :param name:
        :return:
        """
        result_one = self.web_driver.find_elements_by_class_name(ClassName.database_list)
        for result_one_text in result_one:
            if str(name) in result_one_text.text:
                result_two = result_one_text.find_elements_by_class_name(ClassName.ivu_btn)
                result_two[1].click()
                time.sleep(2)
                self.web_driver.find_element_by_xpath(WebControlServer.web_big_data_SQL_list_confirm_del).click()
                time.sleep(4)
                break
            else:
                pass

    def creat_data_list(self, name, sql):
        """
        creat data list
        :param name:
        :param sql:
        :return:
        """
        logger.info("输入SQL语句")
        Common.send_text_by_xpath(self, WebControlServer.web_big_data_SQL_input, sql)
        logger.info("点击执行")
        Common.touch_by_xpath(self, WebControlServer.web_big_data_SQL_run_button)
        logger.info("输入数据及名称")
        row_list = Common.get_results_by_class_name(self, ClassName.ivu_row)[1]
        input_list = Common.get_class_name_elements_by_element(self, row_list, ClassName.ivu_input)
        input_list[0].send_keys(name)
        Common.touch_by_xpath(self, WebControlServer.web_big_data_SQL_list_creat)
        Common.wait(self, 2)

    def cppy_data_list_by_name(self, name):
        """
        根据名称删除数据集内容
        :param name:
        :return:
        """
        result_one = self.web_driver.find_elements_by_class_name(ClassName.data_item)
        for result_one_text in result_one:
            if str(name) in result_one_text.text:
                result_two = result_one_text.find_elements_by_class_name(ClassName.ivu_btn)
                result_two[0].click()
                time.sleep(2)
                self.web_driver.find_element_by_xpath(WebControlServer.web_big_data_SQL_list_confirm_del).click()
                time.sleep(4)
                break
            else:
                pass

    def del_data_list_by_name(self, name):
        """
        根据名称删除数据集内容
        :param name:
        :return:
        """
        result_one = self.web_driver.find_elements_by_class_name(ClassName.data_item)
        for result_one_text in result_one:
            if str(name) in result_one_text.text:
                result_two = result_one_text.find_elements_by_class_name(ClassName.ivu_btn)
                result_two[1].click()
                time.sleep(2)
                self.web_driver.find_element_by_xpath(WebControlServer.web_big_data_SQL_list_confirm_del).click()
                time.sleep(4)
                break
            else:
                pass

    def touch_text_by_class_name(self, class_name, click_text, tag_name=None, times=1):
        """
        touch text by class name
        :param class_name: class name
        :param text: text
        :return:
        """
        try:
            if tag_name is None:
                class_name_result = self.web_driver.find_elements_by_class_name(class_name)
            else:
                class_name_result = self.web_driver.find_elements_by_css_selector("%s[class='%s']" % (tag_name, class_name))
            i = 0
            for class_name_content in class_name_result:
                if click_text == class_name_content.text:
                    i = i + 1
                    if i == times:
                        class_name_content.click()
                        break
            logger.info("通过class_name点击%s成功" % click_text)
            time.sleep(2)
        except:
            logger.info("通过class_name点击%s失败" % click_text)
        Common.wait(self, 2)

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
    def send_text_by_element(self, element, text, clear=True):
        """
        send text by element
        :param element:
        :param name:
        :return:
        """
        if clear:
            element.clear()
        element.send_keys(text)

    @staticmethod
    def send_text_in_window(self, text):
        """
        在光标处输入
        :param text:
        :return:
        """
        keyboard.type_string(text)

    @staticmethod
    def press_enter_in_window(self):
        """
        模拟点击回车
        :return:
        """
        keyboard.tap_key(keyboard.enter_key)

    def switch_iframe(self, iframe):
        """
        switch iframe by name/id/element
        :param iframe:
        :return:
        """
        self.web_driver.switch_to_frame(iframe)

    def switch_default_iframe(self):
        """
        switch to default iframe
        :return:
        """
        self.web_driver.switch_to_default_content()

    def get_result_if_class_name_exist(self, class_name):
        """
        get result if class name exist
        :param class_name:
        :return: True or False
        """
        try:
            self.web_driver.find_elements_by_class_name(class_name)
            return True
        except:
            return False

    def touch_class_name_by_name(self, name, tag_name, class_name):
        """
        touch class name by name
        :param name: tag_name
        :return:
        """
        get_text_row = Common.get_results_by_class_name(self, ClassName.ivu_table_row)
        for text in get_text_row:
            if name in text.text:
                para_ele = text
                break
        view_button = Common.get_class_name_elements_by_element_blank(self, para_ele, tag_name, class_name)[0]
        Common.touch_by_element(self, view_button)

    def get_element_by_placeholder_and_class_name(self, class_name, placeholder):
        """
        get element by placeholder and class_name
        :param class_name:
        :param placeholder:
        :return:
        """
        try:
            get_ele_all = Common.get_results_by_class_name(self, class_name)
            for every_ele in get_ele_all:
                if every_ele.get_attribute("placeholder") == placeholder:
                    logger.info("获取元素成功")
                    return every_ele
        except:
            logger.info("获取元素失败")

    def get_elements_by_placeholder_and_class_name(self, class_name, placeholder):
        """
        get element by placeholder and class_name
        :param class_name:
        :param placeholder:
        :return:
        """
        placeh = []
        try:
            get_ele_all = Common.get_results_by_class_name(self, class_name)
            for every_ele in get_ele_all:
                if every_ele.get_attribute("placeholder") == placeholder:
                    logger.info("获取元素成功")
                    placeh.append(every_ele)
        except:
            logger.info("获取元素失败")
        return placeh

    def touch_by_class_name_and_palceholder(self, class_name, placeholder):
        """
        touch element by placeholder and class_name
        :param class_name:
        :param placeholder:
        :return:
        """
        try:
            get_ele_all = Common.get_results_by_class_name(self, class_name)
            for every_ele in get_ele_all:
                if every_ele.get_attribute("placeholder") == placeholder:
                    logger.info("获取元素成功")
                    every_ele.click()
                    break
        except:
            logger.info("获取元素失败")

    def send_text_by_class_name_and_palceholder(self, class_name, placeholder, text, clear=True):
        """
        send element by placeholder and class_name
        :param class_name:
        :param placeholder:
        :return:
        """
        try:
            get_ele_all = Common.get_results_by_class_name(self, class_name)
            for every_ele in get_ele_all:
                if every_ele.get_attribute("placeholder") == placeholder:
                    logger.info("获取元素成功")
                    if clear:
                        every_ele.clear()
                    every_ele.send_keys(text)
                    break
        except:
            logger.info("获取元素失败")
        Common.wait(self, 3)

    def clear_text_by_class_name_and_placeholder(self, class_name, placeholder, clear=True):
        """
        clear element by placeholder and class_name
        :param class_name:
        :param placeholder:
        :return:
        """
        try:
            get_ele_all = Common.get_results_by_class_name(self, class_name)
            for every_ele in get_ele_all:
                if every_ele.get_attribute("placeholder") == placeholder:
                    logger.info("获取元素成功")
                    if clear:
                        every_ele.clear()
                    every_ele.click()
                    every_ele.send_keys("11")
                    Common.press_backspace_in_window(self, 2)
                    break
        except:
            logger.info("获取元素失败")

    @staticmethod
    def entry_info_in_data_page(self, num, content):
        """
        entry info in data entry page
        :param self:
        :param num:
        :return:
        """
        for i in range(num):
            if i == 0:
                input_result = Common.get_result_by_class_name(self, ClassName.ivu_input)
                Common.send_text_by_element(self, input_result, content+"_%s" % i)
                continue
            ele_1 = Common.get_result_by_class_name_blank(self, "button", ClassName.btn_add_ivu_btn_info)
            Common.touch_by_element(self, ele_1)
            input_result = Common.get_results_by_class_name(self, ClassName.ivu_input)[i]
            Common.send_text_by_element(self, input_result, content+"_%s" % i)
        ele_2 = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_primary)
        Common.touch_by_element(self, ele_2)
        Common.wait(self, 3)

    def touch_id_by_element(self, id, element):
        """"""
        ele = element.find_element_by_id(id)
        Common.touch_by_element(self, ele)

    def get_element_by_class_name_and_text(self, tag_name, class_name, text):
        """
        get element by class_name and text
        :param class_name:
        :param text:
        :return:
        """
        try:
            div_list = Common.get_results_by_class_name_blank(self, tag_name, class_name)
            for con in div_list:
                if text in con.text:
                    return con
        except:
            logger.info("get element failed")
            return False

    def get_elements_by_class_name_and_text(self, tag_name, class_name, text):
        """
        get element by class_name and text
        :param class_name:
        :param text:
        :return:
        """
        a_list = []
        try:
            div_list = Common.get_results_by_class_name_blank(self, tag_name, class_name)
            for con in div_list:
                if text in con.text:
                    a_list.append(con)
            return a_list
        except:
            logger.info("get element failed")

    def touch_edit_by_approval_name(self, name):
        """
        in approval mangament page (approval)
        touch edit by name
        :param name:
        :return:
        """
        div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for con in div_list:
            logger.info(con.text)
            if name in con.text:
                para = con
                break
        ele_para = Common.get_class_name_elements_by_element_blank(self, para, "button",
                                                                   ClassName.ivu_btn_primary_small)[0]
        Common.touch_by_element(self, ele_para)

    def touch_edit_by_group_name(self, name):
        """
        in approval mangament page (group)
        touch edit by name
        :param name:
        :return:
        """
        div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.group)
        for con in div_list:
            logger.info(con.text)
            if name in con.text:
                para = con
                break
        ele_para = Common.get_class_name_elements_by_element_blank(self, para, "div",
                                                                   ClassName.ivu_poptip_rel)[0]
        Common.touch_by_element(self, ele_para)
        return para

    def creat_approval(self, group_name, approval_name, i=0, approval_dis=None):
        """
        creat approval
        :param approval_name: approval name
        :param group_name: created group name
        :param i: approval icon number
        :param approval_dis: approval discription
        :return:
        """
        logger.info("点击创建审批")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "创建新审批", "button")
        logger.info("选择审批图标")
        approval_icon = Common.get_results_by_class_name(self, ClassName.iconitem)
        Common.touch_by_element(self, approval_icon[i])
        logger.info("选择分组与填写审批名称")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, group_name)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入审批名称", approval_name)
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择")
        form_name = Common.get_info_by_sql(self, "select name from scap.form", "scap")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, form_name)
        if approval_dis is not None:
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入审批说明", approval_dis)
        logger.info("点击保存")
        confirm_btn = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)[1]
        Common.touch_by_element(self, confirm_btn)
        Common.wait(self, 2)

    def touch_del_by_approval_name(self, name):
        """
        in approval mangament page (approval)
        touch edit by name
        :param name:
        :return:
        """
        div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for con in div_list:
            logger.info(con.text)
            if name in con.text:
                para = con
                break
        ele_para = Common.get_class_name_elements_by_element_blank(self, para, "button",
                                                                   ClassName.ivu_btn_error_small)[0]
        Common.touch_by_element(self, ele_para)

    def touch_add_process_by_approval_name(self, name):
        """
        in approval mangament page (approval)
        touch edit by name
        :param name:
        :return:
        """
        div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for con in div_list:
            if name in con.text:
                para = con
                break
        ele_para = Common.get_class_name_elements_by_element_blank(self, para, "button",
                                                                   ClassName.ivu_btn_success_small)[0]
        Common.touch_by_element(self, ele_para)

    def get_result_by_id(self, id, tag_name=None):
        """
        get element by id
        :param id:
        :return:
        """
        if tag_name is None:
            return self.web_driver.find_element_by_id(id)
        else:
            return self.web_driver.find_element_by_css_selector("%s[id='%s']" % (tag_name, id))

    def send_text_by_id(self, id_con, text):
        """"""
        id_res = Common.get_result_by_id(self, id_con)
        Common.send_text_by_element(self, id_res, text, False)

    def get_results_by_id(self, id, tag_name=None):
        """
        get element by id
        :param id:
        :return:
        """
        if tag_name is None:
            return self.web_driver.find_elements_by_id(id)
        else:
            return self.web_driver.find_elements_by_css_selector("%s[id='%s']" % (tag_name, id))

    def check_if_id_exist(self, id):
        """"""
        id_results = self.web_driver.find_elements_by_id(id)
        if len(id_results) > 0:
            return True
        else:
            return False

    def touch_by_id(self, id, t=3, times=1):
        """
        touch element by id
        :param id:
        :return:
        """
        element = self.web_driver.find_elements_by_id(id)
        element[times-1].click()
        time.sleep(t)

    def del_created_approval(self, name, confirm=True):
        """
        del created approval
        :param name:
        :param confirm: True : delete, False : cancel
        :return:
        """
        if not Common.check_approval_in_group(self, name, "已停用"):
            Common.stop_approval_by_name(self, name)
        Common.touch_del_by_approval_name(self, name)
        con_and_can = Common.get_result_by_class_name_blank(self, "div", ClassName.ivu_modal_confirm_footer)
        if confirm:
            confirm = Common.get_class_name_elements_by_element_blank(self, con_and_can, "button",
                                                                      ClassName.ivu_btn_large)[0]
            Common.touch_by_element(self, confirm)
        else:
            cancel = Common.get_class_name_elements_by_element_blank(self, con_and_can, "button",
                                                                     ClassName.ivu_btn_text_large)[0]
            Common.touch_by_element(self, cancel)

    def creat_new_group(self, new_group):
        """
        creat new group
        :param new_group:
        :return:
        """
        logger.info("点击新建分组")
        aa = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_ghost)
        Common.touch_by_element(self, aa)
        logger.info("输入分组名称为啊%s的分组" % new_group)
        name_len = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入分组名称")
        Common.send_text_by_element(self, name_len, new_group)
        ok_but = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, ok_but)
        Common.wait(self, 3)

    def check_if_class_name_exist(self, class_name, tag_name=None):
        """
        check if class name exist
        :param class_name:
        :return:
        """
        if tag_name is None:
            cl_na = self.web_driver.find_elements_by_class_name(class_name)
        else:
            cl_na = Common.get_results_by_class_name_blank(self, tag_name, class_name)
        if cl_na is not None:
            logger.info("%s存在" % class_name)
            return True
        else:
            logger.info("%s不存在" % class_name)
            return False

    def check_if_class_name_exist_by_element(self, element, class_name, tag_name=None):
        """
        check if class name exist
        :param class_name:
        :return:
        """
        if tag_name is None:
            cl_na = element.find_elements_by_class_name(class_name)
        else:
            cl_na = element.find_elements_by_css_selector("%s[class='%s']" % (tag_name, class_name))
        if cl_na is not None:
            logger.info("%s存在" % class_name)
            return True
        else:
            logger.info("%s不存在" % class_name)
            return False

    def rename_group_by_name(self, group_name, new_name):
        """
        rename group bu name
        :param group_name:
        :param new_name:
        :return:
        """
        logger.info("点击编辑")
        Common.wait(self, 3)
        Common.touch_edit_by_group_name(self, group_name)
        logger.info("点击重命名")
        new_group = Common.get_element_by_class_name_and_text(self, "div", ClassName.group_list_ivu_row,
                                                              group_name)
        new_group_del = Common.get_class_name_elements_by_element(self, new_group, ClassName.edit_item)
        Common.touch_by_element(self, new_group_del[0])
        Common.wait(self, 5)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入分组名称", new_name)
        ok_but = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, ok_but)

    def del_group_by_name(self, group_name):
        """
        del group by name
        :param group_name:
        :return:
        """
        logger.info("点击编辑")
        Common.wait(self, 3)
        Common.touch_edit_by_group_name(self, group_name)
        logger.info("点击删除")
        new_group = Common.get_element_by_class_name_and_text(self, "div", ClassName.group_list_ivu_row,
                                                              group_name)
        new_group_del = Common.get_class_name_elements_by_element(self, new_group, ClassName.edit_item)
        logger.info(Common.get_text_by_elements(self, new_group_del))
        Common.touch_by_element(self, new_group_del[1])
        Common.wait(self, 5)
        confirm_del_but = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, confirm_del_but[-1])

    def check_approval_in_group(self, approval, group):
        """
        check approval Whether it exists in group
        :param approval: approval name
        :param group: group name
        :return:
        """
        try:
            div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.group_list_ivu_row)
            for group_name in div_list:
                group_name_list = Common.get_class_name_elements_by_element_blank(self, group_name, "div",
                                                                                  ClassName.group)[0]
                if group in group_name_list.text:
                    para = group_name
                    break
            ele_para = Common.get_class_name_elements_by_element(self, para, ClassName.item_content_c)
            ele_para_text = Common.get_text_by_elements(self, ele_para)
            if approval in ele_para_text:
                logger.info("审批存在与指定的分组中")
                return True
            else:
                logger.info("审批未存在与指定的分组中")
                return False
        except:
            logger.info("审批未存在与指定的分组中")
            return False

    def login_web_portal(self, username, password):
        """
        login web portal
        :param username:
        :param password:
        :return:
        """
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", username)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", password)
        # Common.touch_text_by_class_name(self, ClassName.ivu_btn, "获取手机验证码")
        # iden_code = Common.get_identifying_code(self, username)
        # logger.info(iden_code)
        # Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", iden_code)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_long, "登录", "button")

    def login_web_client(self, username, password):
        """
        login web client
        :param username:
        :param password:
        :return:
        """
        if Common.check_if_class_name_exist(self, ClassName.blue_btn):
            Common.touch_text_by_class_name(self, ClassName.blue_btn, "登录", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", username)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", password)
        Common.touch_by_id(self, ID.handleSubmitBtn)
        Common.wait(self, 3)

    def start_approval_by_name(self, name):
        """

        :param name:
        :return:
        """
        created_approval = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for item in created_approval:
            if name in item.text:
                parameter = item
                break
        result = Common.get_class_name_elements_by_element_blank(self, parameter, "button",
                                                                 ClassName.ivu_vtn_warn_small)
        if not result:
            start = Common.get_class_name_elements_by_element_blank(self, parameter, "button",
                                                                    ClassName.ivu_vtn_info_small)
            Common.touch_by_element(self, start[0])
            confirm_start = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
            Common.touch_by_element(self, confirm_start[-1])
            Common.wait(self, 3)

    def stop_approval_by_name(self, name):
        """
        stop approval bu name
        :param name:
        :return:
        """
        created_approval = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for item in created_approval:
            if name in item.text:
                parameter = item
                break
        result = Common.get_class_name_elements_by_element_blank(self, parameter, "button",
                                                                 ClassName.ivu_vtn_warn_small)
        if not result:
            start = Common.get_class_name_elements_by_element_blank(self, parameter, "button",
                                                                    ClassName.ivu_vtn_info_small)
            Common.touch_by_element(self, start[0])
            confirm_start = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
            Common.touch_by_element(self, confirm_start[-1])
            Common.wait(self, 3)
        stop = Common.get_class_name_elements_by_element_blank(self, parameter, "button", ClassName.ivu_vtn_warn_small)
        Common.touch_by_element(self, stop[0])
        confirm_stop = Common.get_results_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, confirm_stop[-1])
        Common.wait(self, 3)

    def get_display_status_by_text(self, text, i=0):
        """
        get display status by text
        :param text:
        :return:
        """
        ele_text = Common.get_results_by_class_name_blank(self, "ul", ClassName.ivu_menu)[i]
        class_name = ele_text.get_attribute("style")
        if "display: none;" in class_name:
            logger.info("%s已经被隐藏" % text)
            return True
        else:
            logger.info("%s未被隐藏" % text)
            return False

    def upload_file(self, class_name, file_type, file_name, count=1):
        """"""
        path_list = {"icon": "\\resource\\Img\\icon\\",
                     "isv": "\\resource\\File\\isv\\",
                     "banner": "\\resource\\Img\\banner\\",
                     "html": "\\resource\\File\\html\\"}
        add_icon = Common.get_results_by_class_name_blank(self, "input", class_name)[count-1]
        add_icon.send_keys(project_path + path_list[file_type] + file_name)

    def touch_search_by_placeholder(self, text):
        """
        touch search button by placeholder
        :param text: content of placeholder
        :return:
        """
        input_and_search = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_input_wrapper_type)
        for i in input_and_search:
            input = Common.get_class_name_elements_by_element_blank(self, i, "input", ClassName.ivu_input)[0]
            if text == input.get_attribute("placeholder"):
                para = Common.get_class_name_elements_by_element_blank(self, i, "i", ClassName.search_icon)[0]
                break
        Common.touch_by_element(self, para)

    def creat_data_item(self, num=1):
        """
        creat data item
        :param num:
        :return:
        """
        for j in range(num):
            logger.info("输入新的数据项")
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加数据项", "button")

            logger.info("输入数据项参数")
            info_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.ivu_table_body)
            info_input = Common.get_class_name_elements_by_element_blank(self, info_ele, "input", ClassName.ivu_input)
            for i in range(len(info_input) - 3, len(info_input), ):
                Common.send_text_by_element(self, info_input[i], "data_para%s" % i)

    def select_area_by_text(self, area_name):
        """
        select area by text
        :param area_name:
        :return:
        """
        area = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_form_item_required, area_name)
        area_list = Common.get_class_name_elements_by_element_blank(self, area, "div", ClassName.ivu_col_span_8)
        for i in area_list:
            Common.touch_by_element(self, i)
            a_list = Common.get_class_name_elements_by_element_blank(self, i, "li", ClassName.ivu_select_item)[0]
            Common.touch_by_element(self, a_list)

    def touch_del_or_edit_in_sql_list_name(self, sql_name, type):
        """
        touch_del_or_edit_in_sql_list_name
        :param sql_name:
        :param type:
        :return:
        """
        data_list = Common.get_result_by_class_name_blank(self, "div", ClassName.database_list)
        text_con = Common.get_class_name_elements_by_element_blank(self, data_list, "label",
                                                                   ClassName.ivu_checkbox_wrapper)
        edit_btn = Common.get_class_name_elements_by_element_blank(self, data_list, "button",
                                                                   ClassName.ivu_vtn_warn_small)
        del_btn = Common.get_class_name_elements_by_element_blank(self, data_list, "button",
                                                                   ClassName.ivu_btn_error_small)
        for i in range(len(text_con)):
            logger.info(text_con[i].text)
            if sql_name in text_con[i].text:
                if type == "edit":
                    Common.touch_by_element(self, edit_btn[i])
                    break
                elif type == "delete":
                    Common.touch_by_element(self, del_btn[i])
                    break
                else:
                    logger.info("type类型为空")
                    break
            else:
                logger.info("根据数据库名称未找到数据库")

    def get_mission_start_time(self):
        """
        Need a time after the current time when creat mission
        :return:
        """
        now = datetime.datetime.now()
        format_time = now + datetime.timedelta(hours=1)
        start_time = datetime.datetime.strftime(format_time, "%Y-%m-%d %H:%M:%S")
        return start_time

    def get_mission_end_time(self):
        """
        get
        :return:
        """
        time1 = Common.get_mission_start_time(self)
        t_time = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
        end_time = t_time + datetime.timedelta(hours=1)
        end_time = datetime.datetime.strftime(end_time, "%Y-%m-%d %H:%M:%S")
        return end_time

    def creat_mission(self, mission_content, executor=True, copyer=None):
        """
        creat mission
        :param mission_content:
        :return:
        """

        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.touch_by_id(self, ID.createTask)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", mission_content)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        if executor:
            Common.touch_by_link_text(self, "指派给自己")
        else:
            choice = Common.get_result_by_class_name_blank(self, "i", ClassName.ivu_icon_plus_circled_icon_normal)
            Common.touch_by_element(self, choice)
            realname1 = Common.get_realname_by_phone(self, Content.spare_count)
            Common.touch_text_by_class_name(self, ClassName.name, realname1, "span")
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        if copyer is not None:
            add_person = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
            Common.touch_tag_name_by_element(self, add_person, "img")
            name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
            Common.touch_text_by_elements(self, name_list, copyer)
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)
        Common.wait(self, 2)

    def open_mission_detail_by_name(self, mission_name, phone_num, num=1):
        """
        mission name
        :param mission_name:
        :return:
        """
        user_id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        mission_id = Common.get_info_by_sql(self, "SELECT id FROM scap.task WHERE creator='%s' AND content='%s'" %
                                            (user_id, mission_name), "scap")
        task_id = ID.viewTask + str(mission_id)
        id_list = Common.get_results_by_id(self, task_id, "div")
        logger.info(id_list)
        Common.touch_by_element(self, id_list[num-1])

    def get_mission_status_by_name(self, mission_name):
        """
        if mission status done return True, else return False
        :param mission_name:
        :return: True/False
        """
        task_list = Common.get_results_by_class_name_blank(self, "div", ClassName.task_item)
        for i in task_list:
            task_name = Common.get_class_name_elements_by_element_blank(self, i, "div", ClassName.task_item_name)[0]
            if task_name.text == mission_name:
                done = Common.get_class_name_elements_by_element_blank(self, i, "span",
                                                                         ClassName.task_status_done)
                undone = Common.get_class_name_elements_by_element_blank(self, i, "span",
                                                                       ClassName.task_status_undone)
                done = list(filter(None, done))
                undone = list(filter(None, undone))
                break
        if done is not None:
            return True
        elif undone is not None:
            return False

    def transmit_mission(self):
        """
        转发之人为出现列表的第一人，未指定人物
        :return:
        """
        Common.touch_by_id(self, ID.rewardTaskBtn)
        executor_ele = Common.get_results_by_class_name_blank(self, "label",
                                                              ClassName.ivu_checkbox_wrapper_group_item)[0]
        Common.touch_by_element(self, executor_ele)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.wait(self, 2)

    def clear_mission_info_by_sql(self, phone_num):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        Common.connect_sql(self, "DELETE FROM scap.task WHERE creator='%s' OR executor='%s'" % (id, id), "scap")

    def add_copy_people(self, copy_num=1):
        """
        copy_num : add copy person num
        :param copy_num:
        :return:
        """
        copy_ele = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, copy_ele, "li")
        for i in range(int(copy_num)):
            executor_ele = Common.get_results_by_class_name_blank(self, "label",
                                                                  ClassName.ivu_checkbox_wrapper_group_item)[0]
            Common.touch_by_element(self, executor_ele)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

    def del_copy_people(self, num=1):
        """
        copy_num : del copy person num
        :param copy_num:
        :return:
        """
        copy_ele = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, copy_ele, "li")
        for i in range(int(num)):
            executor_ele = Common.get_results_by_class_name_blank(self, "label",
                                                                  ClassName.ivu_checkbox_wrapper_group_item)[0]
            Common.touch_by_element(self, executor_ele)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

    def check_mession_belong_to(self, meeting_theme, type=1):
        """

        :param type: 1 未完成， 2 已完成，3 我发出， 4 我执行， 5 抄送我， 6 我转发
        :param meeting_theme:
        :return:
        """
        type_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_tabs_tabpane)
        theme_result_list = Common.get_class_name_elements_by_element_blank(self, type_list[type-1], "h5",
                                                                            ClassName.list_title)
        theme_list = Common.get_text_by_elements(self, theme_result_list)
        if Common.check_text_in_list(self, theme_list, meeting_theme):
            return True
        else:
            return False

    def touch_tag_name_by_element(self, element, tag_name, times=1):
        """
        touch tag_name by element
        :param element:
        :param tag_name:
        :return:
        """
        i = times-1
        ele = element.find_elements_by_tag_name(tag_name)
        Common.touch_by_element(self, ele[i])
        Common.wait(self, 3)

    def get_tag_name_by_element(self, element, tag_name, times=1):
        """
        touch tag_name by element
        :param element:
        :param tag_name:
        :return:
        """
        ele = element.find_elements_by_tag_name(tag_name)
        if times is None:
            return ele
        else:
            return ele[times - 1]

    def creat_schedule(self, shcedule_content):
        """
        creat schedule
        :param shcedule_content:
        :return:
        """
        Common.touch_by_id(self, ID.toAddScheduleBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入日程内容", shcedule_content)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不重复", "li")
        Common.touch_by_id(self, ID.submitAddScheduleBtn)
        Common.wait(self, 3)

    def open_sechdule_by_name(self, name):
        """
        enter_sechdule_by_name
        :param name:
        :return:
        """
        ele = Common.get_element_by_class_name_and_text(self, "div", ClassName.schedule_item_name_ivu_col_span_14,
                                                        name)
        Common.touch_tag_name_by_element(self, ele, "span")

    def del_sechdule_by_name(self, phone_num):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone_num, "scap")
        Common.connect_sql(self, "delete from scap.schedule WHERE creator='%s'" % id, "scap")

    def touch_del_or_edit_by_sechedule_name(self, schedule, type="edit"):
        """
        touch_del_or_edit_by_sechedule_name
        :param schedule:
        :param type:
        :return:
        """
        sech_list = Common.get_results_by_class_name_blank(self, "div", ClassName.schedule_item)
        edit_list = Common.get_results_by_id(self, ID.updateScheduleBtn)
        delete_list = Common.get_results_by_id(self, ID.deleteScheduleBtn)
        for i in range(len(sech_list)):
            if schedule in sech_list[i].text:
                para = i
        if type == "edit":
            Common.touch_by_element(self, edit_list[para])
        elif type == "delete":
            Common.touch_by_element(self, delete_list[para])
            Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

    def get_start_and_end_time(self, type="minute", time_len=6):
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

    def get_realname_by_phone(self, phone_num):
        """
        get realname by phone
        :param phone_num:
        :return: str
        """
        friend_name = Common.get_info_by_sql(self,
                                                  "select realname from user where phone='%s'" % phone_num,
                                                  "scap")
        return friend_name

    def get_nickname_by_phone(self, phone_num):
        """
        get realname by phone
        :param phone_num:
        :return: str
        """
        friend_name = Common.get_info_by_sql(self,
                                                  "select nickname from user where phone='%s'" % phone_num,
                                                  "scap")
        return friend_name

    def creat_meeting(self, theme, content="meeting_con", area="meeting_area", num=1, name=None, remind=None):
        """"""
        Common.touch_by_id(self, ID.addMeetingBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入会议主题", theme)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入会议内容", content)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入会议地点", area)
        if remind is not None:
            Common.touch_text_by_class_name(self, ClassName.ivu_select_selected_value, "不提醒", remind)
            Common.touch_text_by_class_name(self, ClassName.ivu_select_item, remind, "li")
        add_person = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, add_person, "img")
        if name is None:
            check_box_list = Common.get_results_by_class_name_blank(self, "span", ClassName.ivu_checkbox_inner)
            for i in range(num):
                Common.touch_by_element(self, check_box_list[i])
        else:
            logger.info(name)
            name_list = Common.get_results_by_class_name_blank(self, "label", ClassName.ivu_checkbox_wrapper_group_item)
            Common.touch_text_by_elements(self, name_list, name)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_by_id(self, ID.SubmitAddMeetingBtn)
        Common.wait(self, 3)

    def modify_meeting_time(self, start_time, end_time, theme, creator):
        """modify meeting time by sql"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % creator, "scap")
        sql = "UPDATE scap.conference SET start_time = '%s' , end_time = '%s' WHERE theme = '%s' AND creator = '%s'" % (start_time, end_time, theme, id)
        Common.connect_sql(self, sql, "scap")

    def open_meeting_detail_by_name(self, meeting_theme, type=1):
        """"""
        type_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_tabs_tabpane)
        theme_result_list = Common.get_class_name_elements_by_element_blank(self, type_list[type - 1], "h5",
                                                                            ClassName.list_title)
        Common.touch_text_by_elements(self, theme_result_list, meeting_theme)

    def check_meeting_belong_to(self, meeting_theme, type=1):
        """

        :param type: 1 代表未结束， 2 已取消/已结束/已完成，3 我发出的
        :param meeting_theme:
        :return:
        """
        type_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_tabs_tabpane)
        theme_result_list = Common.get_class_name_elements_by_element_blank(self, type_list[type-1], "h5",
                                                                            ClassName.list_title)
        theme_list = Common.get_text_by_elements(self, theme_result_list)
        if Common.check_text_in_list(self, theme_list, meeting_theme):
            return True
        else:
            return False

    def delete_meeting_record(self, count_phone):
        """
        delete meeting record
        :param meeting_name:
        :param count_phone:
        :return:
        """
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        Common.connect_sql(self, "DELETE FROM scap.conference WHERE creator='%s'" % id, "scap")
        Common.connect_sql(self, "DELETE FROM scap.participant WHERE participant_id = '%s'" % id, "scap")

    def modify_meeting_status_by_sql(self, count_phone, met_theme, met_tpye="1"):
        """
        delete meeting record
        :param meeting_name:
        :param count_phone:
        :return:
        """
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % count_phone, "scap")
        Common.connect_sql(self, "UPDATE scap.`conference` SET STATUS='%s' WHERE theme='%s' AND creator = '%s'" %
                           (met_tpye, met_theme, id), "scap")

    def touch_by_link_text(self, link_text):
        """
        touch by link text
        :param link_text:
        :return:
        """
        text_ele = self.web_driver.find_element_by_link_text(link_text)
        text_ele.click()

    def del_friend_by_sql(self, user_phone, friend_phone):
        """
        delete friend relationship by sql
        :return:
        """
        sql1 = "select id from user where phone='%s'" % user_phone
        user_id1 = Common.get_info_by_sql(self, sql1, "scap")
        sql2 = "select id from user where phone='%s'" % friend_phone
        user_id2 = Common.get_info_by_sql(self, sql2, "scap")
        del_sql1 = "delete from friend where user_id='%s' and friend_id='%s'" % (user_id1, user_id2)
        del_sql2 = "delete from friend where user_id='%s' and friend_id='%s'" % (user_id2, user_id1)
        Common.connect_sql(self, del_sql1, "scap")
        Common.connect_sql(self, del_sql2, "scap")

    def creat_friend_by_sql(self, user_phone, friend_phone):
        """
        delete friend relationship by sql
        :return:
        """
        now = Common.get_mission_start_time(self)
        sql1 = "select id from user where phone='%s'" % user_phone
        user_id1 = Common.get_info_by_sql(self, sql1, "scap")
        sql2 = "select id from user where phone='%s'" % friend_phone
        user_id2 = Common.get_info_by_sql(self, sql2, "scap")
        creat_sql1 = "INSERT INTO scap.friend(user_id, friend_id, create_time, update_time) VALUES('%s', '%s', '%s', '%s')"\
                   % (user_id1, user_id2, now, now)
        creat_sql2 = "INSERT INTO scap.friend(user_id, friend_id, create_time, update_time) VALUES('%s', '%s', '%s', '%s')" \
                   % (user_id2, user_id1, now, now)
        Common.connect_sql(self, creat_sql1, "scap")
        Common.connect_sql(self, creat_sql2, "scap")

    def add_friend_in_group(self, num=1):
        """"""
        Common.touch_by_id(self, ID.showSelectPersonModelBtn)
        check_box_list = Common.get_results_by_class_name_blank(self, "span", ClassName.ivu_checkbox_inner)
        for i in range(num):
            Common.touch_by_element(self, check_box_list[i])
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

    def del_friend_in_creat_group(self, num=1):
        """"""
        check_box_list = Common.get_results_by_class_name_blank(self, "i", ClassName.del_ivu_icon_android_close)
        for i in range(num):
            Common.touch_by_element(self, check_box_list[i])

    def search_friend_by_name(self, name, add=True):
        """
        search new friend by name
        :param name: telephone or realname
        :param add: True 代表在添加好友界面， False代表在好友列表界面
        :return:
        """
        if add:
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入电话号码搜索", name)
            Common.touch_by_id(self, ID.searchNewFriendBtn)
        else:
            Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入姓名、电话搜索", name+"\n")

    def get_search_friend_results(self, add=True):
        """
        get search friend result
        :param add: True 代表在添加好友界面， False代表在好友列表界面
        :return:
        """
        if add:
            id_result = Common.get_result_by_id(self, ID.addFriend)
        else:
            id_result = Common.get_result_by_id(self, ID.contactMenu)
        friend_result = Common.get_class_name_elements_by_element_blank(self, id_result, "div", ClassName.friend)
        return friend_result

    def accept_or_not_friend_request(self, phone, accept=True):
        """
        accept or refused friend request
        :param phone:
        :param accept:
        :return:
        """
        name = Common.get_info_by_sql(self, "select realname from scap.user where phone='%s'" % phone, "scap")
        id_result = Common.get_result_by_id(self, ID.friendReq)
        friend_list = Common.get_class_name_elements_by_element_blank(self, id_result, "div", ClassName.friend)
        reject_list = Common.get_results_by_id(self, ID.requestRejectBtn)
        agree_list = Common.get_results_by_id(self, ID.requestAgreeBtn)
        for i in range(len(friend_list)):
            if name in friend_list[i].text:
                num = i
        if accept:
            Common.touch_by_element(self, agree_list[num])
        else:
            Common.touch_by_element(self, reject_list[num])

    def get_friend_request_result(self, phone, exp=True):
        """
        get friend request result , accept or refused
        :param phone:
        :param exp:
        :return:
        """
        name = Common.get_info_by_sql(self, "select realname from scap.user where phone='%s'" % phone, "scap")
        id_result = Common.get_result_by_id(self, ID.friendReq)
        friend_list = Common.get_class_name_elements_by_element_blank(self, id_result, "div", ClassName.text)
        status_list = Common.get_class_name_elements_by_element_blank(self, id_result, "div", ClassName.status)
        for i in range(len(friend_list)):
            if name in friend_list[i].text:
                status = status_list[i].text
        if status == "已添加" and exp:
            return True
        elif status == "已拒绝" and not exp:
            return True
        else:
            logger.info("未对好友请求做任何操作")
            return False

    def del_friend_request_by_sql(self, phone):
        """
        delete friend request by sql , only delete info when statue=0
        :param phone:
        :return:
        """
        friend_id = Common.get_info_by_sql(self, "select id from scap.user where phone='%s'" % phone, "scap")
        Common.connect_sql(self, "delete from scap.friend_request where friend_id='%s'" % friend_id, "scap")

    def creat_friend_requset_by_sql(self, sender, receiver):
        """
        creat friend request by sql,
        :param sender:
        :param receiver:
        :return:
        """
        sender_id = Common.get_info_by_sql(self, "select id from scap.user where phone='%s'" % sender, "scap")
        receiver_id = Common.get_info_by_sql(self, "select id from scap.user where phone='%s'" % receiver, "scap")
        Common.connect_sql(self, "insert into friend_request(request_id, friend_id, status, is_read) VALUES()"
                           % (sender_id, receiver_id, 0, 1))

    def get_frist_app_name(self):
        """
        获取第一个已启用的app名称
        :return:
        """
        app_name = Common.get_info_by_sql(self, "select name from app_entity", "application_center")
        Common.connect_sql(self,
                                "update application_center.app_entity set run_state='1' where name = '%s'" % app_name,
                                "application_center")
        return app_name

    def open_app_detail_by_by_name(self, app_name):
        """"""
        app_card_list = Common.get_results_by_class_name(self, ClassName.app_card)
        for app_card in app_card_list:
            icon = Common.get_tag_name_by_element(self, app_card, "div")
            name = Common.get_tag_name_by_element(self, app_card, "h5")
            a_icon = Common.get_tag_name_by_element(self, icon, "a")
            if app_name in name.text:
                Common.touch_by_element(self, a_icon)
                break

    def clear_opened_app(self, phone):
        """"""
        user_id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone, "scap")
        Common.connect_sql(self,
                                "DELETE FROM application_center.app_entity_user WHERE user_id='%s'" % user_id,
                                "application_center")

    def set_up_nickname_by_user(self, phone, nickname):
        """"""
        sql = "UPDATE scap.user SET nickname='%s' WHERE phone='%s'" % (nickname, phone)
        Common.connect_sql(self, sql, "scap")

    def check_app_evaluation_content_by_user(self, phone, eva_content):
        """"""
        Common.wait(self, 3)
        if phone is not None:
            nick_name = Common.get_nickname_by_phone(self, phone)
        else:
            nick_name = "匿名"
        evaluation_list = Common.get_results_by_class_name_blank(self, "div", ClassName.comment_card)
        logger.info(evaluation_list)
        for command_card in evaluation_list:
            nickname = Common.get_class_name_elements_by_element_blank(self, command_card, "span",
                                                                       ClassName.name_toleft)[0]
            eva_con = Common.get_class_name_elements_by_element_blank(self, command_card, "p", ClassName.content)[0]
            if nick_name == nickname.text and eva_content == eva_con.text:
                return True
        return False

    def report_screen_shot(self, case_name):
        """"""
        try:
            config = configparser.ConfigParser()
            config.read(config_path)
            srceen_shot_path = config.get("screenShot", "screenshot_folder_name")
            screen_shot_name = case_name[:-3] + ".png"
            self.web_driver.get_screenshot_as_file(srceen_shot_path + "/" + screen_shot_name)
        except:
            logger.info("截图失败或者单独运行时不截图")
        logger.info("-------------------%s test finish------------------" % case_name)

    def del_report_template_by_user(self, phone):
        """"""
        id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone, "scap")
        Common.connect_sql(self, "DELETE FROM scap.report_template_user_rl WHERE user_id='%s'" % id, "scap")

    def del_app_entity_by_name(self, app_name):
        """"""
        sql = "delete from app_entity where name='%s'" % app_name
        if "%" in app_name:
            sql = "delete from app_entity where name like '{}'".format(app_name)
        Common.connect_sql(self, sql, "application_center")

    def del_app_classify_by_name(self, classify):
        """"""
        sql = "delete from app_classify where name='%s'" % classify
        Common.connect_sql(self, sql, "application_center")

    def del_dict_standard_by_str_name(self, str_name):
        """"""
        sql = "delete from dict_standard where field_name='%s'" % str_name
        if "%" in str_name:
            sql = "delete from dict_standard where field_name like '{}'".format(str_name)
        Common.connect_sql(self, sql, "scap")

    def del_dict_theme_by_name(self, theme_name):
        """"""
        sql = "delete from dict_theme where name='%s'" % theme_name
        Common.connect_sql(self, sql, "scap")

    def clear_evaluation_by_user(self, phone):
        """"""
        user_id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % phone, "scap")
        sql = "DELETE FROM application_center.app_comment WHERE user_id='%s'" % user_id
        Common.connect_sql(self, sql, "application_center")

    def delete_department_by_name(self, department_name):
        """"""
        sql = "DELETE FROM scap.department WHERE NAME='%s'" % department_name
        Common.connect_sql(self, sql, "scap")

    def modify_user_locked_status_by_phone(self, phone, status="0"):
        """"""
        sql = "UPDATE scap.user SET is_locked='%s' WHERE phone='%s'" % (status, phone)
        Common.connect_sql(self, sql, "scap")

    def delete_role_group_by_name(self, group_name):
        """"""
        sql = "DELETE FROM scap.role WHERE name='%s'" % group_name
        Common.connect_sql(self, sql, "scap")

    def rename_user_realname_by_phone(self, phone, realname):
        """"""
        sql = "UPDATE scap.user SET realname='%s' WHERE phone='%s'" % (realname, phone)
        Common.connect_sql(self, sql, "scap")

    def delete_file_in_window(self, file):
        try:
            os.remove(file)
            logger.info("删除成功")
        except:
            logger.info("删除失败，未找到文件")

    def refresh(self, t=5):
        """
        refersh the page
        :t : wait t second after refresh page
        :return:
        """
        self.web_driver.refresh()
        time.sleep(t)

    def quit(self):
        """停止"""
        self.web_driver.quit()
