from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x) -> str: 
    
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    answer = calc(x)
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(5)
    browser.quit()