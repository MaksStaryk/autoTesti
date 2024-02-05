import time

from selenium.webdriver.common.by import By

from main import sum


def test_1():
    assert sum([5, 5, 7]) == 17

def test_contacts(chrome, our_website):
    """идем вниз в строку и находим доп.инфор. об Ozon """

    time.sleep(3)
    element_is_help = chrome.find_element(By.CSS_SELECTOR, "[class='j0a d6p h8d']")
    chrome.execute_script("arguments[0].scrollIntoView();", element_is_help)
    element_under_house = chrome.find_elements(By.CSS_SELECTOR, "[class='d0i'] div:nth-child(1)")
    time.sleep(1)
    for  index, value in enumerate(element_under_house):
        #assert element.is_displayed(), 'No work'
        print()
        print({index}, {value})
def test_contacts(chrome, our_website):
    """идем вниз в строку и находим доп.инфор. об Ozon """

    time.sleep(5)
    element_is_help = chrome.find_element(By.CSS_SELECTOR, "[class='j0a d6p h8d']")
    chrome.execute_script("arguments[0].scrollIntoView();", element_is_help)
    element_under_house = chrome.find_elements(By.CSS_SELECTOR, "[class='d0i'] div:nth-child(1)")
    time.sleep(3)
    ignore_element = chrome.find_element(By.CSS_SELECTOR, "[class='d0i'] div:nth-child(1) a:nth-child(5)")

    for element in element_under_house:

        print(f"\n Найден недопустимый элемент '{ignore_element.text}'")

    assert ignore_element.is_enabled(), "no work"


