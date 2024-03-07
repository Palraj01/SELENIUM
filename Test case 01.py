import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)
