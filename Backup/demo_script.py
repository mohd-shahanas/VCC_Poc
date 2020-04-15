import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def my_click(element, text):
    element.click()
    print(text + " Clicked")
    time.sleep(5)

def get_table_contents(table_element):
    table_rows = table_element.find_elements_by_tag_name("tr")
    data = {}

    for row in table_rows:
        key = row.find_element_by_tag_name("th").text.strip()
        value = row.find_element_by_tag_name("td").text.strip()
        data[key] = value

    return data


driver = webdriver.Chrome("D:/Projects/VCC_Automation/POC/Utilites/chromedriver")

try:
    # **************************************  LOGIN    ******************************************
    driver.get("https://cem.visualcommandcenter.com")
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, 'UserName')))

    username = driver.find_element_by_id("UserName")
    password = driver.find_element_by_id("Password")
    signin = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/section/form/div[4]/div/div/input")

    username.send_keys("mohammed.shahanas@accionlabs.com")
    password.send_keys("Accion@0420")

    my_click(signin,"signin")
    WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.CLASS_NAME, 'VFApplicationControl-HeaderLogo')))

    print("Login Success")
    time.sleep(20)

    # **************************************  LOGIN ENDS   ******************************************

    # ***********************************  Individual Components    *********************************

    menu = driver.find_element_by_css_selector(".vf-button-minor[title='Open VCC Menu']")
    items = driver.find_element_by_xpath('//div[text()="Items"]')
    feeds = driver.find_element_by_xpath('//div[text()="Feeds"]')
    timeline = driver.find_element_by_xpath('//div[text()="Timeline"]')

    alerts = driver.find_element_by_class_name("AlertsFeedControlSection-Label")
    assets = driver.find_element_by_xpath('//div[@class="FeedControlSection-Label"][text()="Assets"]')
    risk_events = driver.find_element_by_xpath('//div[@class="FeedControlSection-Label"][text()="RISK EVENTS"]')
    context = driver.find_element_by_xpath('//div[@class="FeedControlSection-Label"][text()="CONTEXT"]')

    assets_buildings= driver.find_element_by_xpath('//div[@class="LabeledSymbolCheckBox-Label"][text()="Buildings"]')
    assets_travel = driver.find_element_by_xpath('//div[@class="LabeledSymbolCheckBox-Label"][text()="Travel"]')
    #
    # assets_buildings_items = driver.find_elements_by_class_name("DataPanelCardView-Card")
    #
    # item_edit_button = driver.find_element_by_xpath('//div[@class="MenuBarControlCell-Icon"][@title="Edit item"]')
    # item_edit_fields = driver.find_elements_by_class_name("InputFieldView")

    my_click(menu, "menu")
    my_click(menu, "menu")
    my_click(assets, "assets")
    my_click(assets_buildings, "assets_buildings")
    my_click(assets_travel, "assets_travel")
    my_click(assets_buildings, "assets_buildings")
    my_click(assets_travel, "assets_travel")
    my_click(timeline, "timeline")
    my_click(risk_events, "risk_events")
    my_click(alerts, "alerts")
    my_click(context, "context")
    my_click(items, "items")
    my_click(feeds, "feeds")
    my_click(feeds, "feeds")
    my_click(timeline, "timeline")
    my_click(items, "items")

    # assets_buildings_items = driver.find_elements_by_class_name("DataPanelCardView-Card")
    # print(len(assets_buildings_items))
    # for item in assets_buildings_items:
    #     print(item)

    # ***********************************  Individual Components Ends   *********************************
    assets = driver.find_element_by_xpath('//div[@class="FeedControlSection-Label"][text()="Assets"]')
    my_click(assets, "assets")

    assets_buildings = driver.find_element_by_xpath('//div[@class="LabeledSymbolCheckBox-Label"][text()="Buildings"]')
    my_click(assets_buildings, "assets_buildings")

    items = driver.find_element_by_xpath('//div[text()="Items"]')
    my_click(items, "items")

    assets_buildings_items = driver.find_elements_by_class_name("DataPanelCardView-Card")
    while (len(assets_buildings_items) < 1):
        time.sleep(5)
        assets_buildings_items = driver.find_elements_by_class_name("DataPanelCardView-Card")
    my_click(assets_buildings_items[1],"Building Item")

    assets_buildings_details = driver.find_element_by_class_name("VccDetailsGrid-Table")
    table_data = get_table_contents(assets_buildings_details)
    print(table_data)
    original_contact = table_data['Contact']

    item_edit_button = driver.find_element_by_xpath('//div[@class="MenuBarControlCell-Icon"][@title="Edit item"]')
    my_click(item_edit_button, "item_edit_button")

    item_edit_fields = driver.find_elements_by_class_name("InputFieldView")
    contact_item = item_edit_fields[3]
    contact_item_text = contact_item.find_element_by_class_name("vf-input-text")
    contact_item_text.clear()
    contact_item_text.send_keys(original_contact + "_test")
    time.sleep(10)

    save_button = driver.find_element_by_xpath('//div[@class="DefaultFeedItemEditorControl-Button vf-button-text vf-button-bold"][text()="Save"]')
    save_button.click()

    time.sleep(20)

    my_click(menu, "menu")
    about_vcc = driver.find_element_by_xpath('//div[@class="AppMenuButtonGridButton-Label"][text()="About VCC"]')
    my_click(about_vcc,"about_vcc")



except Exception as msg:
    print("Error found : " + str(msg))

finally:
    driver.close()
