import time

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

    def enable_alerts(self):
        alerts_section = self.driver.find_element_by_class_name("AlertsFeedControlSection-Check")
        alerts_cb = alerts_section.find_element_by_class_name("CheckBox-Check")
        if alerts_cb.get_attribute("data-state") == "checkUnchecked":
            vcc_click(alerts_cb,"Alerts Cb")
        else:
            print("All Alerts are already enabled")

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

    def enable_buildings(self):
        self.expand_assets()
        vcc_click(self.driver.find_element_by_xpath(conf.ASSETS_BUILDINGS), "Buildings")

    def enable_travel(self):
        self.expand_assets()
        vcc_click(self.driver.find_element_by_xpath(conf.ASSETS_TRAVEL), "Travel")

    def get_alert_visible_count(self):
        return self.driver.find_element_by_class_name(conf.VISIBLE_ALERTS_COUNT).text

    def get_alert_total_count(self):
        return self.driver.find_element_by_class_name(conf.TOTAL_ALERTS_COUNT).text

    def display_visible_alerts(self):
        visible_alerts = self.driver.find_elements_by_class_name(conf.VISIBLE_ALERTS)
        for _id, alert in enumerate(visible_alerts):
            print((_id,alert.text))
