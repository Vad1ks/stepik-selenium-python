from selenium import webdriver
import time
import math

def calc(x) -> str: 
    
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    answer = calc(x)
    browser.find_element_by_id("answer").send_keys(answer)

    browser.find_element_by_id("robotCheckbox").click()
    browser.execute_script("window.scroll(0,200);")
    browser.find_element_by_id("robotsRule").click()
    
    button = browser.find_element_by_tag_name("button")
    
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
