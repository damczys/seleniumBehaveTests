from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def startUp():
    driver = webdriver.Firefox()
    driver.get("https://www.netwars.pl")
    locator = ".topic_list th:nth-child(1)"
    driver.set_page_load_timeout(30)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        print (element.text)
    finally:
        driver.quit()

startUp()
