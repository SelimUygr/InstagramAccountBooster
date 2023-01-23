from CreateBrowser import configure_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
from Configuration import get_username,get_password


def login(browser = configure_browser()):
  try:
    username = get_username()
    password = get_password()
    browser.get("https://www.instagram.com/accounts/login/")
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input"))))
    element.send_keys(username)
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input"))))
    element.send_keys(password)
    element.send_keys(Keys.ENTER)
    #Remember button click on not now
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"))))
    element.click()
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))))
    element.click()
    sleep(1)
    return browser


  except TimeoutException:
    print("150 seconds passed element still not there!")



