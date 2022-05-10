# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# В поля будут вставляться рандомные города
        element.send_keys(random.choice(city_list))

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла