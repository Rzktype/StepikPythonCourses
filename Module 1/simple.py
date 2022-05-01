from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

    #  важно понимать только то, что даже если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае.
    #  Советуем добавлять такую обработку ко всем своим скриптам при выполнении задач этого и следующего модулей.