from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture
def app_languages():
    return {
    "en": ["English", "Add to basket"],
    "es": ["Spanish", "Añadir al carrito"],
    "fr": ["French", "Ajouter au panier"]
}

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose one of supported languages: en(English), es(Spanish), fr(French)")


@pytest.fixture(scope="function")
def browser(request, app_languages):
    options = Options()    
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = None
    if user_language in app_languages:
        print(f"\nstart chrome browser with {app_languages[user_language][0]} language for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--language should be one of supported languages: en(English), es(Spanish), fr(French)")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def user_language(request):
    return request.config.getoption("language")
    