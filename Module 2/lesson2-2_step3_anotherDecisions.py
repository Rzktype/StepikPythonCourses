# 1
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    Select(browser.find_element(By.ID, "dropdown"))\
        .select_by_value(str(num2 + num1))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    #  Выведет в консоль номер решения
    print(browser._switch_to.alert.text)

finally:
    sleep(5)
    browser.quit()

# 2
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/selects1.html
link = 'http://suninjuly.github.io/selects1.html'
# link = 'http://suninjuly.github.io/selects2.html'
browser.get(link)

# Посчитать сумму заданных чисел
valueSelect = str(int(browser.find_element_by_css_selector('span#num1').text) + int(browser.find_element_by_css_selector('span#num2').text))

# Выбрать в выпадающем списке значение равное расчитанной сумме
Select(browser.find_element_by_tag_name('select')).select_by_value(valueSelect)

# Нажать кнопку "Отправить"
browser.find_element_by_css_selector('button.btn').click()

# 3 O_o
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)

x = str(eval('+'.join([i.text for i in browser.find_elements(by=By.CLASS_NAME, value="nowrap") if i.text.isdigit()][-3:])))
Select(browser.find_element(by=By.TAG_NAME, value="select")).select_by_value(x)
browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()

# 4
def get_answer(browser):
    """
    Получаем решение
    :param browser: webdriver
    :return: результат
    """
    # browser.get('http://suninjuly.github.io/selects1.html')
    browser.get('http://suninjuly.github.io/selects2.html')
    summ = sum(map(int, [browser.find_element_by_css_selector(s).text for s in
                         ('#num1', '#num2')]))
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(summ))
    browser.find_element_by_css_selector('.btn').click()
    # смотрим всплывающее окно и берем из него результат
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    alert.accept()
    return result
