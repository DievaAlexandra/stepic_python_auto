import self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

#ЭТО НЕ РАБОТАЕТ Я ХЗ ПОЧЕМУ
class TestFindLocator(unittest.TestCase):  # создаем класс, который наследуется от от класса testCase
    def test_abs1(self):
        link1 = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > [placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > [placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > [placeholder='Input your email']")
        input3.send_keys("fdsfds@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert str("Congratulations! You have successfully registered!") == welcome_text, \
            "Should be absolute value of a number"
        browser.quit()

    def test_abs2(self):
        link2 = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > [placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > [placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > [placeholder='Input your email']")
        input3.send_keys("fdsfds@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert str("Congratulations! You have successfully registered!") == welcome_text, \
            "Should be absolute value of a number"
        browser.quit()


if __name__ == '__main__':
    unittest.main()
