import time
import logging
from random import randrange

from dynaconf import settings as conf
from Vcc.Library.CommonUtilities import *

log = logging.getLogger(__name__)

class BottomPanelActions:
    def __init__(self,driver=None):
        self.driver = driver

    def bp_initialize(self,driver):
        log.info("Initializing driver variable for Bottom Panel keywords")
        self.driver = driver

    def select_items_panel(self):
        try:
            log.info("Selecting/Expanding Items tab from bottom panel")
            item_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[0]
            if item_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
                vcc_click(item_cb,"Items")
            else:
                log.info("Items Tab already selected")

        except Exception as msg:
            log.info(str(msg))

    def select_feeds_panel(self):
        try:
            log.info("Selecting/Expanding Feeds Panel ")
            feeds_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[1]
            if feeds_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
                vcc_click(feeds_cb,"Feeds")
            else:
                log.info("Feeds Panel already selected")

        except Exception as msg:
            log.info(str(msg))

    def select_timeline_panel(self):
        try:
            log.info("Selecting/Expanding Timeline tab from bottom panel")
            timeline_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[2]
            if timeline_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkUnchecked":
                vcc_click(timeline_cb,"Timeline")
            else:
                log.info("Timeline Panel already selected")

        except Exception as msg:
            log.info(str(msg))

    def deselect_items_panel(self):
        try:
            log.info("Deselecting/Hiding Items tab")
            item_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[0]
            if item_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
                vcc_click(item_cb,"Items")
            else:
                log.info("Items tab already deselected")

        except Exception as msg:
            log.info(str(msg))

    def deselect_feeds_panel(self):
        try:
            log.info("Deselecting/Hiding Feeds Panel")
            feeds_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[1]
            if feeds_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
                vcc_click(feeds_cb,"Feeds")
            else:
                log.info("Feeds Panel already deselected")

        except Exception as msg:
            log.info(str(msg))

    def deselect_timeline_panel(self):
        try:
            log.info("Deselecting/Hiding Timeline panel")
            timeline_cb = self.driver.find_elements_by_class_name(conf.PANEL_CHECKBOX)[2]
            if timeline_cb.find_element_by_class_name(conf.PANEL_CB_CHECK).get_attribute("data-state") == "checkChecked":
                vcc_click(timeline_cb,"Timeline")
            else:
                log.info("Timeline Panel already deselected")

        except Exception as msg:
            log.info(str(msg))

    def get_items_from_item_panel(self):
        try:
            log.info("Retrieving Items Heading displayed in Item panel")
            item_text = []
            panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
            for item in panel_items:
                item_text.append(item.find_element_by_xpath('//div[@class="VccDetailsVerticalLayout-Heading"][@data-id="_heading"]').text)

            log.info(f"{item_text}")

        except Exception as msg:
            log.info(str(msg))

    def get_item_count(self):
        try:
            log.info("Retrieving the count of Items displayed in Item panel")
            filter_icon = self.driver.find_elements_by_class_name("ItemTypeFilterButton")
            final_count = 0
            for item in filter_icon:
                item_count = item.find_element_by_xpath('//div[@data-id="_countView"]').text
                final_count = final_count + int(item_count)
            log.info(f"Total count = {final_count}")
            return final_count

        except Exception as msg:
            log.info(str(msg))

    def get_building_item_details(self, item_no):
        try:
            log.info("Retrieving the details of Item selected")
            panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
            count = 0
            while len(panel_items) < 1 and count < 10:
                count += 1
                time.sleep(5)
                panel_items = self.driver.find_elements_by_class_name(conf.ITEMS_PANEL_VIEW)
            vcc_click(panel_items[int(item_no)], "Item" + item_no)

            selected_item_details = self.driver.find_element_by_class_name(conf.ITEMS_ITEM_TABLE)
            return get_table_contents(selected_item_details)

        except Exception as msg:
            log.info(str(msg))

    def edit_building_contact_details(self):
        try:
            log.info("Editing Building contact details")
            item_edit_button = self.driver.find_element_by_xpath(conf.ITEMS_DETAILS_EDIT)
            vcc_click(item_edit_button, "item_edit_button")

            item_edit_fields = self.driver.find_elements_by_class_name(conf.ITEMS_EDIT_ELEMENTS)
            contact_item = item_edit_fields[3]
            contact_item_text = contact_item.find_element_by_class_name(conf.ITEMS_EDIT_TEXTBOX)
            contact_item_text.clear()
            contact_item_text.send_keys("Stefanie Smith_"+str(randrange(100)))
            time.sleep(5)

            save_button = self.driver.find_element_by_xpath(conf.ITEMS_EDIT_SAVE)
            vcc_click(save_button,"Save")
            time.sleep(5)

            self.close_edit_window()

        except Exception as msg:
            log.info(str(msg))

    def close_edit_window(self):
        try:
            log.info("Going back from the Edit Window")
            edit_back_btn = self.driver.find_element_by_class_name(conf.ITEMS_DETAILS_BACK_BTN)
            vcc_click(edit_back_btn, "Back Btn")

        except Exception as msg:
            log.info(str(msg))

    def get_scalebar_display_status(self):
        try:
            log.info("Retrieving the display status of Scalebar - True/False")
            style_attributes = self.driver.find_element_by_class_name(conf.SCALE_BAR).get_attribute("style").split(';')
            if style_attributes[1].strip() == "display: none":
                return False
            else:
                return True

        except Exception as msg:
            log.info(str(msg))

    def click_download(self):
        try:
            log.info("Downloading the File..")
            download_btn = self.driver.find_element_by_xpath('//div[@data-id="_contentZone"][text()="Download"]')
            vcc_click(download_btn,"Download")

        except Exception as msg:
            log.info(str(msg))


