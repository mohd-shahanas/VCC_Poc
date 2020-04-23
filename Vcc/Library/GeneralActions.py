import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dynaconf import settings as conf
from Vcc.Library.CommonUtilities import *


class GeneralActions():
    def __init__(self):
        self.driver = None

    def user_login(self, username=conf.VCC_USERNAME, password=conf.VCC_PASSWORD):
        try:

            # chromeOptions = Options()
            # chromeOptions.add_experimental_option("prefs",{"download.default_directory" : conf.DOWNLOAD_FOLDER})
            # self.driver = webdriver.Chrome(executable_path=conf.CHROMEDRIVER, chrome_options=chromeOptions)
            self.driver = webdriver.Chrome(executable_path=conf.CHROMEDRIVER)

        except Exception as msg:
            print(msg)

        try:
            self.driver.get(conf.VCC_URL)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.ID, conf.USERNAME)))

            self.driver.find_element_by_id(conf.USERNAME).send_keys(username)
            self.driver.find_element_by_id(conf.PASSWORD).send_keys(password)
            vcc_click(self.driver.find_element_by_xpath(conf.SIGNIN), "Signin")

            WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located((By.CLASS_NAME, conf.VCC_LOGO)))

            print("Login Success")
            time.sleep(20)

        except Exception as msg:
            print(msg)
            self.driver.close()
            return None

        return self.driver

    def general_initialize(self, driver):
        self.driver = driver

    def refresh_home_page(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located((By.CLASS_NAME, conf.VCC_LOGO)))

        print("Refresh Success")

    def user_logout(self):
        self.driver.close()
