from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

text = "semper posuere integer et senectus justo curabitur."

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_iframe(driver):

    wait = WebDriverWait(driver, 10)

    frames = driver.find_elements(By.TAG_NAME, "iframe")
    assert frames, "No frames found"

    driver.switch_to.frame(frames[0])

    body = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    assert text in body.text