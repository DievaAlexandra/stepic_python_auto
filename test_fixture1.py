from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():
    #ТО ЕСТЬ СНАЧАЛА МЫ ПРОПИСЫВАЕМ ФИКСТУРУ И ЗАТЕМ УЖЕ ШАГИ ТЕСТА
    @classmethod
    # это часть по установке браузера, мы ее выделили в фикстуру.
    # в принте выводим то что будет в консоли выводится
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
    #и закрытие бразуера тоже в фикстуру.
    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

#ТУТ БРАУЗЕР ДЛЯ ПЕРВОГО КЛАССА ЗАПУСТИТСЯ ОДИН РАЗ,
# А ДЛЯ ВТОРОГО КЛАССА ДВА РАЗА ПОТОМУ ЧТО ТАМ НЕТ classmethod
