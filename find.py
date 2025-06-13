from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

def findLink(driver, link2, text):
    driver.get(link2)
    link = driver.find_element(By.PARTIAL_LINK_TEXT, text)
    link.click()