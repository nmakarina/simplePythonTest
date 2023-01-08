from selenium import webdriver
import os
import time

#инстанс webDriver'а для Chrome
Instance = None

def initialize():
    currentDir = os.getcwd()
    global Instance
    Instance = webdriver.Chrome(executable_path=currentDir + "\chromedriver\chromedriver.exe")

    Instance.maximize_window()
    Instance.implicitly_wait(5)
    return Instance


def closeDriver():
    global Instance
    Instance.quit()


def clearCookies():
    global Instance
    Instance.delete_all_cookies()
    time.sleep(5)