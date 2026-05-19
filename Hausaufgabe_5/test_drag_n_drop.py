from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep


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

    iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe)

    trash = driver.find_element(By.ID, "trash")
    first_img = driver.find_element(By.XPATH, "//img[contains(@alt, 'The peaks of High Tatras')]")
    gallery_images = driver.find_elements(By.CSS_SELECTOR, "#gallery li h5:before")

    actions = ActionChains(driver)
    actions.drag_and_drop(first_img, trash).release().perform()

    for el in gallery_images:
        print(el.text)

    print(len(gallery_images))



    assert len(gallery_images) == 3
