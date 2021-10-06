from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

def calc(x) -> str: 
    
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ждем пока цена не станет равна 100
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    browser.find_element_by_id('book').click()

    # решаем пример
    x = int(browser.find_element_by_id('input_value').text)
    answer = calc(x)
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(5)
    browser.quit()