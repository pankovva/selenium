from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x.get_attribute("valuex")
    x = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(x)
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotsRule.click()

    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()