from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Посчитать сумму заданных чисел
    x1 = browser.find_element(By.ID, "num1")
    x2 = browser.find_element(By.ID, "num2")
    sum = int(x1.text) + int(x2.text)
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    # Нажать на кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()
    # Проверяем, все либо загрузилось
    time.sleep(3)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
