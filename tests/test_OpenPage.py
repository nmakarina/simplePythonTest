from core import AttachHelper
from helpers import LoginHelper
import allure
from allure import severity, severity_level

URL = "http://yourURL.com"


class TestOpenPageClass:


    @allure.feature('Открытие страницы логина')
    @severity(severity_level.NORMAL)
    def test_1(self):
        """
        step 1:
            Переход на страницу логина

        """
        range2 = '0'
        with allure.step("переход на страницу логина"):
            LoginHelper.OpenURL(URL)

            result = LoginHelper.LoginPageIsOpen()

            if (result==False):
                AttachHelper.AllureAttachPNG()
            assert(result == True)

