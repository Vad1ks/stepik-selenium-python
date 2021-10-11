from selenium import webdriver
import time


class TestLanguages():

    def test_button_is_present(self, browser: webdriver):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        add_to_cart_button = browser.find_element_by_class_name("btn-add-to-basket")
        assert add_to_cart_button, "There is no add_to_cart_button on site"

    def test_text_on_add_to_cart_button(self, browser: webdriver, app_languages: dict[str, list[str]], user_language: str):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        actual_text = browser.find_element_by_class_name("btn-add-to-basket").text
        expected_text = app_languages[user_language][1]
        #time.sleep(10)
        assert actual_text == expected_text, f"Text is wrong on {app_languages[user_language][0]} version of website"
        