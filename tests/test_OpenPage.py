from core import AttachHelper
from helpers import LoginHelper
import pytest
import allure

URL = "http://yourURL.com"


class TestOpenPageClass:


    @allure.feature('Открытие страницы логина')
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_1(self):
        """
        step 1:
            Переход на страницу логина

        """
        range2 = '0'
        with allure.step("Создание нового бланка"):
            # переход на страницу логина
            LoginHelper.OpenURL(URL)

            result = LoginHelper.LoginPageIsOpen()

            if (result==False):
                AttachHelper.AllureAttachPNG()
            assert(result == True)

