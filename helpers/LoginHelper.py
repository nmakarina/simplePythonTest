from pages.LoginPage import LoginPage
import allure


def OpenURL(url):
    allure.attach(str(url), 'Переход на страницу', 'text/plain')
    LoginPage.goToURL(url)


def LoginPageIsOpen():
    result = LoginPage.findLoginField()
    if (result):
        allure.attach('Открыта страница логина', 'Проверка', 'text/plain')
        return True
    else:
        allure.attach('Страница логина НЕ открыта', 'Ошибка', 'text/plain')
        return False