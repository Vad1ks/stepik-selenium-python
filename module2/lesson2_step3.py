from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

def calc(a,b) -> str: 
  return str(a + b)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element_by_id('num1').text)
    b = int(browser.find_element_by_id('num2').text)
    answer = calc(a,b)

    Select(browser.find_element_by_tag_name("select")).select_by_value(answer)

    browser.find_element_by_css_selector("[type=submit]").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
