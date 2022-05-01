import math, time
from selenium.webdriver.common.by import By
from selenium import webdriver



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

element1 = browser.find_element(By.CSS_SELECTOR, '#answer')
element1.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option2.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
option2.click()

time.sleep(5)
browser.quit()