import pytest
from core import Driver
import allure

@pytest.yield_fixture(scope="function", autouse=True)
def driver():
    allure.attach("Инициализация инстанса web driver", 'Initialize', 'text/plain')
    drv = Driver.initialize()
    yield drv
    allure.attach("Закрытие браузера", 'Close', 'text/plain')
    Driver.closeDriver()


@pytest.fixture(scope="function")
def clearCookies():
    allure.attach("clear", 'cookies', 'text/plain')
    Driver.clearCookies()
