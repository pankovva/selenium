from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

# Работа с окнами

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    #переход на другую вкладку
    browser.switch_to.window(browser.window_handles[1])
    num = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    num = calc(num)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(num)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()