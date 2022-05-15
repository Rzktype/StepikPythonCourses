# 1
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/get_attribute.html
browser.get('http://suninjuly.github.io/get_attribute.html')

# Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()
# 2
import math
import time
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x = browser.find_element_by_id('treasure').get_attribute("valuex")
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
# 3
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    '''
    Функция возращает результат формулы
    :param x:
    :return:
    '''
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(link)

# Находим значение аттрибута valuex элемента "сундук"
x = driver.find_element_by_css_selector('#treasure').get_attribute('valuex')

y = calc(x)

# Передаем в поле ввода результат вычисления функции
driver.find_element_by_css_selector('#answer').send_keys(y)

# Кликаем чекбокс "Подтверждаю, что являюсь роботом"
driver.find_element_by_css_selector('#robotCheckbox').click()

# Кликаем radio "Роботы рулят"
driver.find_element_by_css_selector('#robotsRule').click()

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()