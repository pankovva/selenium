from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
file_name = "summer.txt"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file_name)

with webdriver.Chrome() as browser:
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys("Petr")
    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("petrov@mail.com")
    file = browser.find_element(By.CSS_SELECTOR, "[id='file']")
    file.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()