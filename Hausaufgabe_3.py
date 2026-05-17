from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


# def test_displayed_on_page(driver):
#     wait = WebDriverWait(driver, 5)
#
#     main_icon = driver.find_element(By.CSS_SELECTOR, "a[href='/ru'] img")
#     programs = driver.find_element(By.XPATH, "//span[text()='Программы']")
#     prices = driver.find_element(By.XPATH, "//span[text()='Способы оплаты']")
#     about_us = driver.find_element(By.XPATH, "//span[text()='О нас']")
#
#     about_us.click()
#
#     contacts = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Контакты')]"))
#     )
#     bildungsgutschein = driver.find_element(By.XPATH, "//span[text()='Bildungsgutschein']")
#     reviews = driver.find_element(By.XPATH, "//span[text()='Отзывы']")
#     blog = driver.find_element(By.XPATH, "//span[text()='Блог']")
#
#     assert main_icon.is_displayed()
#     assert programs.is_displayed()
#     assert prices.is_displayed()
#     assert about_us.is_displayed()
#     assert contacts.is_displayed()
#     assert bildungsgutschein.is_displayed()
#     assert reviews.is_displayed()
#     assert blog.is_displayed()
#
#
# def test_language_switcher(driver):
#     wait = WebDriverWait(driver, 5)
#
#     de_btn = driver.find_element(By.XPATH, "//a[text()='de']")
#     de_btn.click()
#
#     wait.until(EC.url_to_be("https://itcareerhub.de/"))
#     assert driver.current_url == "https://itcareerhub.de/"
#
#     ru_btn = driver.find_element(By.XPATH, "//a[text()='ru']")
#     ru_btn.click()
#
#     wait.until(EC.url_to_be("https://itcareerhub.de/ru"))
#     assert driver.current_url == "https://itcareerhub.de/ru"



def test_callback(driver):
    wait = WebDriverWait(driver, 10)
    about_us = driver.find_element(By.XPATH, "//span[text()='О нас']")
    about_us.click()
    contacts = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Контакты')]")))
    contacts.click()
    call_back = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='ОБРАТНЫЙ ЗВОНОК']")))
    driver.execute_script("arguments[0].click();", call_back)

    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#molecule-175871291755985340")))
    modal_text = modal.text
    assert "Запишитесь на бесплатную карьерную консультацию" in modal_text




