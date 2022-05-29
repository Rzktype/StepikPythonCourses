"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1) Открыть страницу http://suninjuly.github.io/alert_accept.html
2) Нажать на кнопку
3) Принять confirm
4) На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button") # Жмём кнопку для вызова модалки
button.click()

confirm = browser.switch_to.alert # Переходим к модалке и кликаем "Ок"
confirm.accept()

x_element = browser.find_element(By.ID, "input_value") # берем Х из капчи и считаем по формуле
x = x_element.text
y = calc(x)

element1 = browser.find_element(By.ID, "answer") # отправляем ответ из капчи
element1.send_keys(y)

element2 = browser.find_element(By.TAG_NAME, "button")
element2.click()

time.sleep(5)

browser.quit()

"""
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
        #return str(math.log(abs(12*math.sin(int(x)))))
        return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
browser.switch_to.alert.accept()
x = browser.find_element(By.ID, "input_value").text
y = calc(int(x))
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
sleep (5)
browser.quit
"""