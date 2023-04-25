from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    #получаем число
    num = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    num = calc(num)
    #пишем ответ
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(num)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    _ = button.location_once_scrolled_into_view
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotsRule.click()

    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()