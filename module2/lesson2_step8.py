from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys('name')
    browser.find_element_by_name("lastname").send_keys('last name')
    browser.find_element_by_name("email").send_keys('email')

    open('newfile.txt', "x").close() # создаём , если отсутствует
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'newfile.txt')           # добавляем к этому пути имя файла 
    browser.find_element_by_id("file").send_keys(file_path)
    
    button = browser.find_element_by_css_selector("[type=submit]")
    
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    os.remove('newfile.txt')
    # закрываем браузер после всех манипуляций
    browser.quit()
