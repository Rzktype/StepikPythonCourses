"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:
1) Открыть страницу http://suninjuly.github.io/redirect_accept.html
2) Нажать на кнопку
3) Переключиться на новую вкладку
4) Пройти капчу для робота и получить число-ответ
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button") # Жмём кнопку для перехода на новую вкладку
button.click()
time.sleep(1)

new_window = browser.window_handles[1] # Переключаемся на 2ую вкладку браузера
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value") # берем Х из капчи и считаем по формуле
x = x_element.text
y = calc(x)

element1 = browser.find_element(By.ID, "answer") # отправляем ответ из капчи
element1.send_keys(y)

element2 = browser.find_element(By.TAG_NAME, "button")
element2.click()

time.sleep(2)

confirm = browser.switch_to.alert # Переходим к модалке и кликаем "Ок"
confirm.accept()

time.sleep(1)

browser.quit()