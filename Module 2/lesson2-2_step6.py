"""
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

1) Открыть страницу http://SunInJuly.github.io/execute_script.html.
2) Считать значение для переменной x.
3) Посчитать математическую функцию от x.
4) Проскроллить страницу вниз.
5) Ввести ответ в текстовое поле.
6) Выбрать checkbox "I'm the robot".
7) Переключить radiobutton "Robots rule!".
8) Нажать на кнопку "Submit".
"""

import math
from selenium.webdriver.common.by import By
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value') # ищем по id чему равен X
x = x_element.text # берём значение
y = calc(x) # считаем по формуле

element1 = browser.find_element(By.ID, 'answer') # находим поле куда нужно отправить ответ из формулы
element1.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox") # Выбрать checkbox "I'm the robot"
option1.click()

button = browser.find_element(By.TAG_NAME, "button") # листаем страницу что-бы было видно Submit и robotsRule
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

option2 = browser.find_element(By.ID, "robotsRule") # Переключить radiobutton "Robots rule!"
option2.click()

button.click() # Нажать на кнопку "Submit"