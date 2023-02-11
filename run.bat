rd /s /q reports
rd /s /q reports_allure
rd /s /q reports_junit
md reports
md reports_allure
md reports_junit

set PYTHONPATH=%CD%

%CD%\venv\Scripts\py.test --junitxml=reports_junit/test_OpenPage.xml --alluredir=reports/ tests/test_OpenPage.py

::libs\allure-2.3.4\bin\allure.bat generate -o reports_allure/ -- reports/
pause

