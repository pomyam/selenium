from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    element = browser.find_element(By.CSS_SELECTOR, "button")
    element.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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
