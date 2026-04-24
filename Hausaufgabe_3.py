from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pytest


"""1. Открывает https://itcareerhub.de/ru"""


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()




def test_open_site(driver):
    sleep(1)

"""2. Проверяет, что на странице отображаются:
  -  Логотип ITCareerHub
  -  Ссылка “Программы”
  -  Ссылка “Способы оплаты”
  -  Ссылка “О нас”
  -  Ссылка “Контакты”
  -  Ссылка “Отзывы”
  -  Ссылка “Блог”
  -  Кнопки переключения языка (ru и de)
"""

def test_displayed_on_page(driver):
    wait = WebDriverWait(driver, 10)
    main_icon = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 > div > div > div.t396__elem.tn-elem.tn-elem__19217104631710153310155 > a > img")
    programs = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426165569250 > a > div > span")
    prices = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426166311940 > a > div > span")
    about_us = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426166799010 > a > div > span")

    about_us.click()

    contacts = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rec2183881603 > div > div > div.t794__content > ul > li:nth-child(2) > a")))
    reviews = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__19217104631773659569108000001 > a > div > span")
    blog = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426168494440 > a > div > span")
    buttons = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 > div > div > div.t396__elem.tn-elem.tn-elem__19217104631710152941400 > a")



    assert main_icon.is_displayed()
    assert programs.is_displayed()
    assert prices.is_displayed()
    assert about_us.is_displayed()
    assert contacts.is_displayed()
    assert reviews.is_displayed()
    assert blog.is_displayed()
    assert buttons.is_displayed()

    sleep(3)




""" 3. Кликнуть по разделу “Контакты”
    4. Кликнуть по кнопке “Обратный звонок”
    5. Проверить что текст “Запишитесь на бесплатную карьерную консультацию” отображается во всплывающем окне. """

def test_gutschein_click(driver):
    wait = WebDriverWait(driver, 10)
    about_us = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426166799010 > a > div > span")
    about_us.click()
    sleep(1)
    contacts = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rec2183881603 > div > div > div.t794__content > ul > li:nth-child(2) > a")))
    contacts.click()
    sleep(3)
    call_back = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rec1194986741 > div > div > div.t396__elem.tn-elem.tn-elem__11949867411754046238620 > a")))
    driver.execute_script("arguments[0].click();", call_back)
    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#molecule-175871291756044240 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1862496483175871291756015470 > div")))
    modal_text = modal.text
    assert "Запишитесь на бесплатную карьерную консультацию" in modal_text
