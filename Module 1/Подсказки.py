print('Подсказки селениум')

# Поля класса By, которые можно использовать для поиска:
"""
By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
"""
# Xpath selector
print('XPath-селектор, чтобы выбрать только кнопку с текстом Gold.')
# //*[text()="Gold"] или  //button[text()="Gold"] или //button[contains(text(), "Gold")]



"""
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
"""

#существуют методы find_elements_by, которые в отличие от find_element_by вернут список всех найденных элементов по заданному условию

"""
Набор стратегий здесь такой же, как и в случае с find_element_by:

find_elements_by_css_selector;
find_elements_by_xpath;
find_elements_by_name;
find_elements_by_tag_name;
find_elements_by_class_name;
find_elements_by_link_text;
find_elements_by_partial_link_text.
Также для поиска нескольких элементов мы можем использовать универсальный метод find_elements вместе с атрибутами класса By:

from selenium.webdriver.common.by import By

browser.find_elements(By.CSS_SELECTOR, "button.submit")
"""
 #Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements.
  #если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException,
  #которая прервёт выполнение вашего кода.
  #Второй же метод всегда возвращает валидный результат: если ничего не было найдено,
  #то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.