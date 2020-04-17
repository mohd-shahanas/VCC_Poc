import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dynaconf import settings as conf
from Vcc.Library.CommonUtilities import *


class MenuActions():
    def __init__(self):
        self.driver = None
        self.default_window = None

    def mp_initialize(self, driver):
        self.driver = driver
        self.default_window = self.driver.current_window_handle

    def click_menu(self):
        vcc_click(self.driver.find_element_by_xpath(conf.MENU), "Menu")

    def get_menu_grid_element(self, category, tab_name):
        sections = self.driver.find_elements_by_class_name(conf.MENU_GRID_SECTIONS)
        _category = None

        for section in sections:
            if section.find_element_by_class_name(conf.MENU_GRID_SECTION_TITLE).text == category:
                _category = section
        category_items = _category.find_elements_by_class_name(conf.MENU_GRID_BUTTON)

        for item in category_items:
            if item.find_element_by_class_name(conf.MENU_GRID_BUTTON_LABEL).text == tab_name:
                return item

        return None

    def get_menu_list_element(self, category, tab_name):
        sections = self.driver.find_elements_by_class_name(conf.MENU_LIST_SECTIONS)
        _category = None

        for section in sections:
            if section.find_element_by_class_name(conf.MENU_LIST_SECTION_TITLE).text == category:
                _category = section
        category_items = _category.find_elements_by_class_name(conf.MENU_LIST_BUTTON)

        for item in category_items:
            if item.find_element_by_class_name(conf.MENU_LIST_BUTTON_LABEL).text == tab_name:
                return item

        return None

    def is_preference_tab_selected(self, tab_name):
        tab_element = self.get_menu_grid_element("PREFERENCES", tab_name)
        if tab_element.get_attribute("data-selected") == '':
            return True
        else:
            return False

    def select_preference_tab(self, tab_name):
        if self.is_preference_tab_selected(tab_name):
            print("Already selected")
        else:
            tab_element = self.get_menu_grid_element("PREFERENCES", tab_name)
            vcc_click(tab_element,tab_name)

    def deselect_preference_tab(self, tab_name):
        if self.is_preference_tab_selected(tab_name):
            tab_element = self.get_menu_grid_element("PREFERENCES", tab_name)
            vcc_click(tab_element, tab_name)
        else:
            print("Already Deselected")

    def click_tools_tab(self, tab_name):
        saved_views = self.get_menu_grid_element("TOOLS", tab_name)
        vcc_click(saved_views, tab_name)

    def get_saved_views(self):
        saved_views = self.driver.find_element_by_class_name(conf.SAVED_VIEW_LIST)
        saved_views_items = saved_views.find_elements_by_class_name(conf.SAVED_VIEW_ROW_TITLE)
        saved_views_list = [item.text for item in saved_views_items]
        return saved_views_list

    def create_new_saved_view(self, title):
        '''
        existing_views = self.get_item_list()
        if title in existing_views:
            print(title + " already present")
            return
        '''
        new_view_btn = self.driver.find_element_by_class_name(conf.CREATE_NEW_VIEW_BTN)
        vcc_click(new_view_btn, "Create New View Btn")
        self.driver.find_element_by_xpath(conf.CREATE_VIEW_TITLE_TB).send_keys(title)

        saved_view_minor_btn = self.driver.find_element_by_class_name(conf.SAVED_VIEW_MINOR_BTN)
        visible_to_others_cb = saved_view_minor_btn.find_element_by_class_name(conf.VISIBLE_TO_OTHERS_CB)
        vcc_click(visible_to_others_cb, "Visible to other cb")

        save_btn = self.driver.find_element_by_xpath(conf.SAVE_NEW_VIEW)
        vcc_click(save_btn,"Save Btn")
        time.sleep(10)

    def validate_created_item(self, old_list, new_list, new_item):
        print("Old List - {}".format(old_list))
        print("New List - {}".format(new_list))
        assert list(set(new_list)-set(old_list))[0] == new_item

    def close_saved_view_tab(self):
        close_btn = self.driver.find_element_by_class_name(conf.CLOSE_SAVED_VIEW)
        vcc_click(close_btn,"Close Btn")

    def click_launch_apps_tab(self, tab_name):
        saved_views = self.get_menu_list_element("LAUNCH APPS", tab_name)
        vcc_click(saved_views, tab_name)

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.default_window:
                self.driver.switch_to.window(handle)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "CreateLinkControl")))

    def switch_to_default_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.default_window)
        time.sleep(5)

    def get_item_list(self):
        self.scroll_down()
        time.sleep(5)
        items = self.driver.find_elements_by_class_name("ListController-ItemTitle")
        return [item.text for item in items]

    def scroll_down(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def create_new_note(self, title):
        '''
        existing_notes = self.get_item_list()
        if title in existing_notes:
            print(title + " already present")
            return
        '''
        new_note_btn = self.driver.find_element_by_class_name("CreateLinkControl")
        vcc_click(new_note_btn, "New Note")
        time.sleep(5)

        self.driver.find_element_by_xpath('//input[@class="vf-input-text"][@data-id="_title"]').send_keys(title)

        create_btn = self.driver.find_element_by_xpath('//div[@data-id="_createButton"]')
        vcc_click(create_btn,"Create Btn")

        text_in_notes_editor = "Header\nSection\nSubsection"
        self.driver.find_element_by_id("NoteEditor-EditorControl").send_keys(text_in_notes_editor)
        time.sleep(5)

        save_btn = self.driver.find_element_by_xpath('//div[@data-id="_saveButton"]')
        vcc_click(save_btn, "Save Btn")

        back_to_main = self.driver.find_element_by_class_name("BackLinkControl-Icon")
        vcc_click(back_to_main, "Back Btn")

    def create_new_checklist(self, title):
        '''
        existing_checklist = self.get_item_list()
        if title in existing_checklist:
            print(title + " already present")
            return
        '''
        new_checklist_btn = self.driver.find_element_by_class_name("CreateLinkControl")
        vcc_click(new_checklist_btn, "New Note")
        time.sleep(5)

        self.driver.find_element_by_xpath('//input[@class="vf-input-text"][@data-id="_title"]').send_keys(title)

        create_btn = self.driver.find_element_by_xpath('//div[@data-id="_createButton"]')
        vcc_click(create_btn,"Create Btn")

        back_to_main = self.driver.find_element_by_class_name("BackLinkControl-Icon")
        vcc_click(back_to_main, "Back Btn")

