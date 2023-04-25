from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#
#
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    _ = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    #ищем число
    num = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    num = calc(num)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(num)
    button = browser.find_element(By.ID, "solve")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()