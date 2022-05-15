"""
Для этой задачи мы придумали еще один вариант капчи для роботов.
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

- Напишите код, который реализует следующий сценарий:
1) Открыть страницу http://suninjuly.github.io/selects1.html
2) Посчитать сумму заданных чисел
3) Выбрать в выпадающем списке значение равное посчитанной сумме
4) Нажать кнопку "Submit"

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже должен пройти успешно.
"""
# Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку!


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1") # Нашли первое число
x = x_element.text
y_element = browser.find_element(By.ID, "num2") # Нашли второе число
y = y_element.text
result = int(x) + int(y) # Считаем сумму
select = Select(browser.find_element(By.ID, "dropdown")) # Переходим к списку
select.select_by_visible_text(str(result)) # Выбираем число из х+у

button = browser.find_element(By.XPATH, "//button[text()='Submit']") # Отправить
button.click()