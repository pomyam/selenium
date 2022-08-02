from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу https://suninjuly.github.io/math.html
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    field = browser.find_element(By.CSS_SELECTOR, ".form-control")
    field.send_keys(y)
    # Отметить checkbox "I'm the robot"
    button1 = browser.find_element(By.ID, "robotCheckbox")
    button1.click()
    # Выбрать radiobutton "Robots rule!"
    button2 = browser.find_element(By.ID, "robotsRule")
    button2.click()
    # Нажать на кнопку Submit
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()
    # Проверяем, все либо загрузилось
    time.sleep(3)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
