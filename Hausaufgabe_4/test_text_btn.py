from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_text_btn(driver):
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    blue_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    input_field.send_keys("ITCH")

    blue_btn.click()
    assert blue_btn.text == "ITCH"