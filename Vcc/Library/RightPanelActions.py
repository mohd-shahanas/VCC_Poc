import time
from random import randrange

from dynaconf import settings as conf
from Vcc.Library.CommonUtilities import *
from Vcc.Library.BottomPanelActions import BottomPanelActions


class RightPanelActions:
    def __init__(self):
        self.driver = None
        self.bpobj = None

    def rp_initialize(self, driver):
        self.driver = driver
        self.bpobj = BottomPanelActions(driver)

    def expand_alerts(self):
        self.bpobj.select_feeds_panel()
        vcc_click(self.driver.find_element_by_class_name(conf.ALERTS), "Alert")

    def expand_assets(self):
        self.bpobj.select_feeds_panel()
        vcc_click(self.driver.find_element_by_xpath(conf.ASSETS), "Assets")

    def expand_risk_events(self):
        self.bpobj.select_feeds_panel()
        vcc_click(self.driver.find_element_by_xpath(conf.RISK_EVENTS), "Risk Events")

    def expand_context(self):
        self.bpobj.select_feeds_panel()
        vcc_click(self.driver.find_element_by_xpath(conf.CONTEXT), "Context")

    def get_check_box_element(self, label):
        feed_section = self.driver.find_elements_by_xpath('//div[@class="FeedControlSection"]')
        req_section = ''
        for section in feed_section:
            if section.find_element_by_class_name("FeedControlSection-Label").text == label:
                req_section = section
        return req_section.find_element_by_class_name("CheckBox-Check")

    def get_feed_count(self,label):
        feed_section = self.driver.find_elements_by_xpath('//div[@class="FeedControlSection"]')
        req_section = ''
        for section in feed_section:
            if section.find_element_by_class_name("FeedControlSection-Label").text == label:
                req_section = section
        return req_section.find_element_by_class_name("FeedControlSection-Count").text

    def enable_alerts(self):
        alerts_section = self.driver.find_element_by_class_name("AlertsFeedControlSection-Check")
        alerts_cb = alerts_section.find_element_by_class_name("CheckBox-Check")
        if alerts_cb.get_attribute("data-state") == "checkUnchecked":
            vcc_click(alerts_cb,"Alerts Cb")
        else:
            print("All Alerts are already enabled")
        time.sleep(20)

    def disable_alerts(self):
        alerts_section = self.driver.find_element_by_class_name("AlertsFeedControlSection-Check")
        alerts_cb = alerts_section.find_element_by_class_name("CheckBox-Check")
        if alerts_cb.get_attribute("data-state") == "checkUnchecked":
            print("All Alerts are already disabled")
        else:
            vcc_click(alerts_cb, "Alerts Cb")

    def enable_all_assets(self):
        assets_cb = self.get_check_box_element("ASSETS")
        if assets_cb.get_attribute("data-state") == "checkUnchecked":
            vcc_click(assets_cb, "Assets Cb")
        else:
            print("All assets are already enabled")

    def enable_all_risk_events(self):
        risk_events_cb = self.get_check_box_element("RISK EVENTS")
        if risk_events_cb.get_attribute("data-state") == "checkUnchecked":
            vcc_click(risk_events_cb, "Risk Events Cb")
        else:
            print("All Risk Events are already enabled")

    def enable_all_context(self):
        context_cb = self.get_check_box_element("CONTEXT")
        if context_cb.get_attribute("data-state") == "checkUnchecked":
            vcc_click(context_cb, "Context Cb")
        else:
            print("All Context are already enabled")

    def disable_all_assets(self):
        assets_cb = self.get_check_box_element("ASSETS")
        if assets_cb.get_attribute("data-state") == "checkUnchecked":
            print("All assets are already disabled")
        else:
            vcc_click(assets_cb, "Assets Cb")

    def disable_all_risk_events(self):
        risk_events_cb = self.get_check_box_element("RISK EVENTS")
        if risk_events_cb.get_attribute("data-state") == "checkUnchecked":
            print("All Risk Events are already disabled")
        else:
            vcc_click(risk_events_cb, "Risk Events Cb")

    def disable_all_context(self):
        context_cb = self.get_check_box_element("CONTEXT")
        if context_cb.get_attribute("data-state") == "checkUnchecked":
            print("All Context are already disabled")
        else:
            vcc_click(context_cb, "Context Cb")

    def click_buildings(self):
        self.expand_assets()
        vcc_click(self.driver.find_element_by_xpath(conf.ASSETS_BUILDINGS), "Buildings")

    def click_travel(self):
        self.expand_assets()
        vcc_click(self.driver.find_element_by_xpath(conf.ASSETS_TRAVEL), "Travel")

    def get_alert_visible_count(self):
        return self.driver.find_element_by_class_name(conf.VISIBLE_ALERTS_COUNT).text

    def get_alert_total_count(self):
        return self.driver.find_element_by_class_name(conf.TOTAL_ALERTS_COUNT).text

    def get_visible_alerts(self):
        visible_alerts = self.driver.find_elements_by_class_name(conf.VISIBLE_ALERTS)
        return [alert.text for alert in visible_alerts]

    def select_visible_alert(self, alert_index):
        visible_alerts = self.driver.find_elements_by_class_name(conf.VISIBLE_ALERTS)
        visible_alerts_list = [(alert.text,alert) for alert in visible_alerts]
        non_duplicate_alerts = []
        duplicate_alerts = []
        for alert in visible_alerts_list:
            if alert[0] in non_duplicate_alerts:
                duplicate_alerts.append(alert[0])
            else:
                non_duplicate_alerts.append(alert[0])

        unique_alerts = list(set(non_duplicate_alerts) - set(duplicate_alerts))
        selected_alert_text = unique_alerts[randrange(len(unique_alerts)-1)]
        for alert in visible_alerts_list:
            if alert[0] == selected_alert_text:
                selected_alert = alert[1]
                break

        vcc_click(selected_alert,"Selected Alert")
        return selected_alert_text

    def click_alert_specific_menu_item(self, menu_item):
        element_xpath ='//div[@class="MenuBarControlCell-Icon"][@title="' + menu_item + '"]'
        menu_element = self.driver.find_element_by_xpath(element_xpath)
        vcc_click(menu_element,menu_item)
        time.sleep(10)

    def add_acknowledge_details(self):
        add_info_tb = self.driver.find_element_by_xpath('//textarea[@class="AlertDialogBase-DetailsText vf-input-text"][@data-id="_message"]')
        add_info_tb.send_keys("Ignore- For UI Test")
        time.sleep(5)
        ack_alert = self.driver.find_element_by_xpath('//div[@class="vf-button-text vf-button-bold"][text()="Acknowledge Alert"]')
        vcc_click(ack_alert, "Acknowledge Alert")

    def check_alert_present(self, alert_title):
        visible_alerts = self.get_visible_alerts()
        return alert_title in visible_alerts

    def click_back_to_alerts(self):
        back_to_alert_btn = self.driver.find_element_by_xpath(
            '//div[@class="AlertDetailsContainer-BackToAlerts vf-button-minor"]')
        vcc_click(back_to_alert_btn, "Back to alert")

    def add_email_details_and_send(self):
        email_tb = self.driver.find_element_by_xpath('//input[@type="text"][@data-id="_additionalContacts"]')
        email_tb.send_keys("kmshahanas007@gmail.com")
        time.sleep(5)

        attachments = self.driver.find_elements_by_class_name("SendMessageDialog-AttachmentCheckBox")
        for item in attachments:
            cb = item.find_element_by_class_name("CheckBox-Check")
            cb_label = item.find_element_by_class_name("CheckBox-Label").text
            vcc_click(cb, cb_label)

        email_btn = self.driver.find_element_by_xpath(
            '//div[@class="vf-button-text vf-button-bold"][text()="Send Email"]')
        vcc_click(email_btn, "Send Email")

        time.sleep(15)

        self.click_back_to_alerts()
        self.bpobj.deselect_items_panel()

    def click_inrix_traffic(self):
        self.expand_risk_events()
        vcc_click(self.driver.find_element_by_xpath(conf.RISK_EVENTS_INRIX_TRAFFIC), "Inrix Traffic")
        time.sleep(10)




