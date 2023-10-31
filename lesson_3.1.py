from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим кнопку
    button = browser.find_element(By.ID, "book")

    # ждем когда цена снизится до 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # нажимаем кнопку Book
    button.click()

    #скроллим вниз
    field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)

    # считаем математическую формулу для x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    print(y)

    # ищем поле для ввода
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # нажимаем submit
    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()


#здесь некий текст, для того чтобы отследить новый коммент. А могла быть ваша рекламаш67ш67ш67ш