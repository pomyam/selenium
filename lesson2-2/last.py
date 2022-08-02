from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name=lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name=email]")
    input3.send_keys("Smolensk")
    # Получаем путь к директории текущего исполняемого файла
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname("./"))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test.txt')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
