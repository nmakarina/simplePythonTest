import allure
from core import Driver


def AllureAttachExeption(e):
    allure.attach(str(e), 'Exception', 'text/plain')
    allure.attach(Driver.Instance.get_screenshot_as_png(), 'Exeption screenshot', 'png')


def AllureAttachPNG():
    allure.attach(Driver.Instance.get_screenshot_as_png(), 'Fail screenshot', 'png')