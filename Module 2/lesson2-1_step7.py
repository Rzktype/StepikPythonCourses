'''
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", точнее,значение хранится в атрибуте valuex у картинки с изображением сундука.
'''
import math
from selenium.webdriver.common.by import By
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '[valuex]') # ищем атрибут у картинки
x = x_element.get_attribute('valuex') # берём значение атрибута
y = calc(x) # считаем по формуле

element1 = browser.find_element(By.ID, 'answer')
element1.send_keys(y)

option1 = browser.find_element(By.ID, 'robotCheckbox') # кликаем чек-бокс I'm the robot
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule") # выбираем radiobutton Robots rule
option2.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']") # отправить
option2.click()

time.sleep(5)
browser.quit()