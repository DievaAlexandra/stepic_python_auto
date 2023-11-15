from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


    def test_login(self):
        link_login = "https://stepik.org/catalog"
        browser.get(link_login)

        login_button = browser.find_element(By.CLASS_NAME, "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
        login_button.click()

        #поиск поля email
        email_field = browser.find_element(By.ID, "id_login_email")
        email_field.send_keys("dieva.sro@mail.ru")

        #поиск поля password
        password_field = browser.find_element(By.ID,"id_login_password")
        password_field.send_keys("Akutnr8!")

        #поиск кнопки "Войти"
        login_button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader ")
        login_button.click()

    @pytest.mark.parametrize('number', ["236896"])
    def test_step_link(self, browser, number):
        links = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(links)
        finally_message = ""

        # поиск текстовой области ответа
        answer_area = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        answer_area.send_keys(math.log(int(time.time())))
        print(answer_area)

        # ждем когда кнопка Отправить будет кликабельной и нажимаем
        wait = WebDriverWait(browser, 15)
        submit_answer_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        submit_answer_button.click()

        # поиск текста "Correct!" на странице НАДО ПЕРЕПИСЫВАТЬ
        text_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text
        text_correct = "Correct!"
        if text_message != text_correct:
            finally_message += text_message
            print(finally_message)
