import time

from dynaconf import settings as conf
from Vcc.Library.CommonUtilities import *


class BottomPanelActions:
    def __init__(self,driver=None):
        self.driver = driver

    def bp_initialize(self,driver):
        self.driver = driver

    def select_items_panel(self):
        item_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[0]
        if item_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
            vcc_click(item_cb,"Items")
        else:
            print("Items Panel already selected")

    def select_feeds_panel(self):
        feeds_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[1]
        if feeds_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
            vcc_click(feeds_cb,"Feeds")
        else:
            print("Feeds Panel already selected")

    def select_timeline_panel(self):
        timeline_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[2]
        if timeline_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
            vcc_click(timeline_cb,"Timeline")
        else:
            print("Timeline Panel already selected")

    def deselect_items_panel(self):
        item_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[0]
        if item_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
            vcc_click(item_cb,"Items")
        else:
            print("Items Panel already deselected")

    def deselect_feeds_panel(self):
        feeds_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[1]
        if feeds_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
            vcc_click(feeds_cb,"Feeds")
        else:
            print("Feeds Panel already deselected")

    def deselect_timeline_panel(self):
        timeline_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[2]
        if timeline_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
            vcc_click(timeline_cb,"Timeline")
        else:
            print("Timeline Panel already deselected")

    def get_items_from_item_panel(self):
        item_text = []
        panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
        for item in panel_items:
            item_text.append(item.find_element_by_xpath('//div[@class="VccDetailsVerticalLayout-Heading"][@data-id="_heading"]').text)

        print(item_text)

    def get_item_count(self):
        filter_icon = self.driver.find_elements_by_class_name("ItemTypeFilterButton")
        final_count = 0
        for item in filter_icon:
            item_count = item.find_element_by_xpath('//div[@data-id="_countView"]').text
            print(item_count)
            final_count = final_count + int(item_count)
        return final_count

    def get_building_item_details(self, item_no):
        panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
        while len(panel_items) < 1:
            time.sleep(5)
            panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
        vcc_click(panel_items[int(item_no)], "Item" + item_no)

        selected_item_details = self.driver.find_element_by_class_name(conf.ITEMS_ITEM_TABLE)
        return get_table_contents(selected_item_details)

    def edit_building_contact_details(self):
        item_edit_button = self.driver.find_element_by_xpath(conf.ITEMS_DETAILS_EDIT)
        vcc_click(item_edit_button, "item_edit_button")

        item_edit_fields = self.driver.find_elements_by_class_name(conf.ITEMS_EDIT_ELEMENTS)
        contact_item = item_edit_fields[3]
        contact_item_text = contact_item.find_element_by_class_name(conf.ITEMS_EDIT_TEXTBOX)
        new_value = contact_item_text.get_attribute('value') + "_1"
        contact_item_text.clear()
        contact_item_text.send_keys(new_value)
        #contact_item_text.send_keys("Stefanie Smith")
        time.sleep(5)

        save_button = self.driver.find_element_by_xpath(conf.ITEMS_EDIT_SAVE)
        vcc_click(save_button,"Save")
        time.sleep(5)

        self.close_edit_window()

    def close_edit_window(self):
        edit_back_btn = self.driver.find_element_by_class_name(conf.ITEMS_DETAILS_BACK_BTN)
        vcc_click(edit_back_btn, "Back Btn")

    def get_scalebar_display_status(self):
        style_attributes = self.driver.find_element_by_class_name(conf.SCALE_BAR).get_attribute("style").split(';')
        if style_attributes[1].strip() == "display: none":
            return False
        else:
            return True

    def click_download(self):
        download_btn = self.driver.find_element_by_xpath('//div[@data-id="_contentZone"][text()="Download"]')
        vcc_click(download_btn,"Download")


