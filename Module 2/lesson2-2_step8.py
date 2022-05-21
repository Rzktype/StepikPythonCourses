from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Находим и заполняем поля
input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("Smolensk@mail.ru")

element = browser.find_element(By.CSS_SELECTOR, "[type='file']") # Находим загрузчик
current_dir = os.path.abspath(os.path.dirname(__file__)) # находим директорию выполняемого скрипта
file_name = "testfile.txt" # имя используемого файла
file_path = os.path.join(current_dir, file_name) # путь до файла
element.send_keys(file_path) # отправляем файл

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)
browser.quit()

