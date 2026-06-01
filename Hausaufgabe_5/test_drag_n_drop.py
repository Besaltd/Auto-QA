from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


def test_drag_and_drop(driver):

    # Закриваємо GDPR попап
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Einwilligen') or contains(., 'Accept') or contains(., 'Zustimmen')]"))).click()
    except:
        pass


    wait = WebDriverWait(driver, 20)

    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(frame)

    source = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.drag_and_drop(source, trash).release().perform()

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3