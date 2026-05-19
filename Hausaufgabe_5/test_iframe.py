from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_iframe(driver):
    text = "semper posuere integer et senectus justo curabitur."
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src='content.html']"))
    )
    driver.switch_to.frame(iframe)

    paragraphs = driver.find_elements(By.TAG_NAME, "p")

    found = False

    for p in paragraphs:
        actual = " ".join(p.text.split())

        if text in actual:
            found = True
            break

    assert found, f"Текст '{text}' не знайдено"
