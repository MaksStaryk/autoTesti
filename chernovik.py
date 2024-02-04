import pytest
from selenium.webdriver import Keys
import time
from conftest import chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from conftest import our_website
from selenium.common.exceptions import NoSuchDriverException

list_other_think =   ["книга","сковородка",
                                   "стиральная машина", "ноутбук"]
num_list = [1,2,3,5]
@pytest.mark.parametrize('other_number', num_list)
def test_poisk_string(chrome, other_number):
    """В строке поиска вводим значения и получаем ошибки"""


    our_website = ("https://ozon.by/")

    element = chrome.find_element(By.XPATH, '//input')
    element.click()

    element.send_keys(other_number, Keys.ENTER)
    time.sleep(3)
    search_everywhere = chrome.find_element(By.CSS_SELECTOR, "[class='vw3']")

    assert search_everywhere.is_displayed() is False