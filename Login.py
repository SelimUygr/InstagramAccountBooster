from CreateBrowser import configure_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from os.path import join,dirname
from dotenv import load_dotenv,find_dotenv



load_dotenv()

username =os.getenv("IG_USERNAME")
password = os.getenv("IG_PASSWORD")


def login(browser=configure_browser()):
  try:
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
    #Explore button
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/a/div"))))
    element.click()
    #Click on first Post 
    # Will get this inside for loop
    for section in range(8):
      for post in range(5):
        element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[{section + 1}]/div[{post + 1}]"))))
        element.click()
        # # Click on likes button 
        # element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span"))))
        # element.click()
        # We will think of something else in here ! And also need to put this code in seperate files this place is for just login for fuck sake man!
        # user_count = 1
        # total_user = 1
        # while user_count < 12: 
        #   first_time = True
        #   if(total_user < 101):
        #     button_text = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[{user_count}]/div[3]/button/div/div"))))
        #     button_text = button_text.text
        #     if(button_text == "Follow"):
        #       element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div"))))
        #       element.click()
        #       if(first_time):
        #         element.send_keys(Keys.ENTER)
        #         first_time = False
        #       for i in range(3):
        #         element.send_keys(Keys.ENTER)
        #         element.send_keys(Keys.ENTER)
        #         element.send_keys(Keys.ENTER)
        #       print("clicked")
        #       sleep(1)
        #       user_count += 1
        #     if(user_count == 12):
        #       user_count -= 1
        #     total_user += 1
        #   else:
        #     break
        sleep(3)
        element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div"))))
        element.click()

        



  except TimeoutException:
    print("150 seconds passed element still not there!")



