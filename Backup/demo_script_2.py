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


driver = webdriver.Chrome("D:/Projects/VCC_Automation/Vcc_Poc/Vcc/Utilites/chromedriver")

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
    time.sleep(30)

    # **************************************  LOGIN ENDS   ******************************************

    # ***********************************  Individual Components    *********************************

    #check_box = driver.find_element_by_xpath('//div[@class="PanelCheckBox CheckBox"]/div[@class="CheckBox-Check CheckGraphic"][text()="Items"]')
    #print(check_box.get_attribute("data-state"))
    # for item in check_boxes:
    #     #     print(item.get_attribute("data-state"))
    #'''
    menu = driver.find_element_by_css_selector(".vf-button-minor[title='Open VCC Menu']")
    my_click(menu, "menu")

    sections = driver.find_elements_by_class_name("AppMenuButtonGridSection")
    print(sections)

    for sec in sections:
        if sec.find_element_by_class_name("AppMenuButtonGridSection-Title").text == 'PREFERENCES':
            preferences = sec

    preferences_items = preferences.find_elements_by_class_name("AppMenuButtonGridButton")

    for item in preferences_items:
        print(item.find_element_by_class_name("AppMenuButtonGridButton-Label").text)
        if item.get_attribute("data-selected") == '':
            print("Selected")
        if item.get_attribute("data-selected") is None:
            print("Not Selected")


    #'''





except Exception as msg:
    print("Error found : " + str(msg))

finally:
    driver.close()
