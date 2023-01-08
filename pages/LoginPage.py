from core import Driver
from core import AttachHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class LoginPage:

    LOGIN_XPATH = "//input[@name='username']"


    @staticmethod
    def goToURL(url):
        Driver.Instance.get(url)
        time.sleep(4)

    @staticmethod
    def findLoginField():
        try:
            Driver.Instance.find_element_by_xpath(LoginPage.LOGIN_XPATH)
            return True
        except Exception as e:
            AttachHelper.AllureAttachExeption(e)
            return False
