#Проматываю страницу к каждому элементу, чтобы не иметь проблем на маленьком экране:
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://SunInJuly.github.io/execute_script.html')

x = int(browser.find_element(By.ID, 'input_value').text)

answer = browser.find_element(By.ID, 'answer')
browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
answer.send_keys(str(math.log(abs(12*math.sin(x)))))

robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
robotCheckbox.click()

robotsRule = browser.find_element(By.ID, 'robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
robotsRule.click()

button = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
button.click()

assert True

# Сохраню потому что понравилась длина кода
from selenium import webdriver
from math import log, sin

link = "https://SunInJuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    y = log(abs(12 * sin(x)))
    ans = browser.find_element_by_tag_name('input')
    ans.send_keys(str(y))
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans)

    for n in ['robotCheckbox', 'robotsRule']:
        browser.find_element_by_id(n).click()
    browser.find_element_by_tag_name("button").click()

    code = browser.switch_to.alert.text
    print(code.split()[-1])


# Полная автоматизация :)

from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    presence_of_all_elements_located as elem_loc
from selenium.webdriver.support.expected_conditions import \
    element_to_be_clickable as elem_click


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def get_answer(browser):
    """
    Получаем решение
    :param browser: webdriver
    :return: результат
    """
    browser.get('http://suninjuly.github.io/execute_script.html')
    x = browser.find_element_by_css_selector('#input_value').text
    print(x, calc(x))
    # перебираем все элементы для кликов
    for select in ['#answer', '#robotCheckbox', '#robotsRule', '.btn']:
        element = browser.find_element_by_css_selector(select)
        # прокручиваем до каждого элемента
        browser.execute_script('return arguments[0].scrollIntoView(true);', element)
        if select == '#answer':
            element.send_keys(calc(x))
        else:
            element.click()
    # смотрим всплывающее окно и берем из него результат
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    # без этого не работает дальнейший переход на степик
    alert.accept()
    return result


def wait_spinner(browser):
    """
    Ждём, пока спиннер пропадёт
    :param browser: webdriver
    :return: None
    """
    driver_wait = WebDriverWait(browser, 9)
    for class_name in ('loader__spinner', 'stepik-loader'):
        driver_wait.until_not(elem_loc((By.CLASS_NAME, class_name)))
    for txt in ('подождите, не покидайте страницу',
                'С этого шага можно безопасно уходить'):
        driver_wait.until_not(elem_loc((By.XPATH,
                                        f'//span[contains(text(),{txt})]')))


def send_answer(browser, result, lesson_url):
    """
    Вставка решения на страницу урока
    :param browser: webdriver
    :param result: текст решения
    :param lesson_url: линк на урок
    :return: None
    """
    login = 'your_login'
    password = 'your_password'
    # идем на страницу авторизации степика
    browser.get('https://stepik.org/catalog?auth=login')
    wait = WebDriverWait(browser, 9)
    submit = wait.until(elem_click((By.CLASS_NAME, 'sign-form__btn.button_with-loader')))
    # логинимся на сайт
    browser.find_element(By.NAME, 'login').send_keys(login)
    browser.find_element(By.NAME, 'password').send_keys(password)
    submit.click()
    wait.until(elem_click((By.CLASS_NAME, 'navbar__profile-img')))
    # идем на страницу урока
    browser.get(lesson_url)
    wait_spinner(browser)
    # если есть решение - обновим
    if browser.find_elements(By.CLASS_NAME, 'again-btn'):
        browser.find_element(By.CLASS_NAME, 'again-btn').click()
        if browser.find_elements(By.CLASS_NAME, 'modal-popup__container'):
            # подтвердим, что хотим решить снова
            browser.find_element_by_xpath('//button[text()="OK"]').click()
            # очистим поле "решение"
            wait.until(elem_click((By.TAG_NAME, "textarea"))).clear()
    # вставка ответа
    wait.until(elem_click((By.TAG_NAME, "textarea"))).send_keys(result)
    # отправка решения
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    wait_spinner(browser)
    if browser.find_elements(By.CLASS_NAME, 'attempt-message_wrong'):
        print('Неверное решение!!!')
        # что-то пошло не так подержим браузер 30 сек
        __import__('time').sleep(30)
    else:
        print('Решено верно!!!')


try:
    browser_driver = webdriver.Chrome()

    # получаем решение
    answer = get_answer(browser_driver)
    print(answer)

    # отправляем решение
    url = 'https://stepik.org/lesson/228249/step/6?unit=200781'
    send_answer(browser_driver, answer, url)

finally:
    browser_driver.quit()