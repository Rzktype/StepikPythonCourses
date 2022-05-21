from selenium import webdriver
import time
import os

try:
    # 1. Открыть страницу http://suninjuly.github.io/file_input.html
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(by='name', value='firstname').send_keys('Vasya')
    browser.find_element(by='name', value='lastname').send_keys('Ivaniv')
    browser.find_element(by='name', value='email').send_keys('Vasya@gmail.com')
    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # file_path.send_keys(file_path)
    browser.find_element(by='name', value='file').send_keys(file_path)
    # 4. Нажать кнопку "Submit"
    browser.find_element(by='class name', value='btn.btn-primary').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(1)
    browser.quit()

#Pathlib вместо os, файл создаем в самом тесте

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

with open('test.txt', 'w') as f:
    print('Selenium - rulezz =)', file=f)
file_to_send = Path('test.txt').resolve().__str__()

url = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    fields = browser.find_elements(By.CSS_SELECTOR, '[type="text"][required]')
    [f.send_keys(f.accessible_name) for f in fields]
    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_to_send)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    print(browser.switch_to.alert.text)

# С циклом для полей
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/file_input.html'
lst = ['pablo', 'xXx', 'pablo@gmail.com']
browser = webdriver.Chrome()
browser.get(url)
inputs = browser.find_elements(By.TAG_NAME, 'input')    # Получаем список всем полей input на странице

for i, l in zip(inputs, lst):   # в этом цикле проходим по списку полей input и  списку с данными
    i.send_keys(l)

file = os.path.abspath(os.path.dirname(__file__))   # положили в переменную путь до папки с проектом G:\Мой диск\selenium\main
file_path = os.path.join(file, 'file.txt')      # склели путь к папке с проектом и имя файла
input_file = browser.find_element(By.ID, 'file') # получили элемент кнопки загрузки файлы
input_file.send_keys(file_path)     # Отправили файл
browser.find_element(By.TAG_NAME, ' button').click()    # нажали на кнопку отправки формы