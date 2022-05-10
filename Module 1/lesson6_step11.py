# Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся.
# Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку.
# Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы
# Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг.

from selenium import webdriver
from selenium.webdriver.common.by import By # Для использования обновлённого синтаксиса
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]") # Ищем поле с именем
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]") # Ищем поле с фамилией
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]") # Ищем поле с почтой
    input3.send_keys("Smolensk@mail.ru")
    time.sleep(5) # Для визуальной проверки какие поля заполнились

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()