from threading import Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

browser = webdriver.Chrome()

link_login = "https://stepik.org/catalog"
browser.get(link_login)
browser.implicitly_wait(10)






# задаем декоратор для параметризации линков задач
@pytest.mark.parametrize('number', ["236895"])
def test_login_link(browser, number):
    links = f"https://stepik.org/lesson/{number}/step/1?auth=login"
    browser.get(links)
    browser.implicitly_wait(15)

    #задаем пустую строку для сообщения
    finally_message = ""

    # поиск поля email
    login_field = browser.find_element(By.ID, "id_login_email")
    login_field.send_keys("dieva.sro@mail.ru")

    # поиск поля "пароль"
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys("Akutnr8!")

    # поиск кнопки "Войти"
    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
    submit_button.click()

    # поиск текстовой области ответа
    answer_area = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer_area.send_keys(math.log(int(time.time())))
    print(answer_area)
    #ждем когда кнопка Отправить будет кликабельной и нажимаем
    wait = WebDriverWait(browser, 15)
    submit_answer_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    submit_answer_button.click()

    #поиск текста "Correct!" на странице НАДО ПЕРЕПИСЫВАТЬ
    text_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text
    text_correct = "Correct!"
    if text_message != text_correct:
        finally_message += text_message
        print(finally_message)


    assert browser.find_element(By.CLASS_NAME, "smart-hints__hint") == text_correct



