import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#здесь мы написали декоратор для языка, чтобы тест прошел дважды с разным значением этого параметра
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    #здесь соответственно он откроет два раза браузер, один с ссылкой в конце ru а второй с en-gb в конце
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.parametrize('language', ["ru", "en-gb"])
    class TestLogin:
        def test_guest_should_see_login_link(self, browser, language):
            link = f"http://selenium1py.pythonanywhere.com/{language}/"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, "#login_link")
            # этот тест запустится 2 раза

        def test_guest_should_see_navbar_element(self, browser, language):
    # этот тест тоже запустится дважды