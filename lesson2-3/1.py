from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Получаем путь к директории текущего исполняемого файла
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)
    # Нажать на кнопку Submit
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
