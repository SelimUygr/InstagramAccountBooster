from ToExplorePage import  WebDriverWait,By,EC,TimeoutException,to_explore
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def follow_from_explore():
  browser = to_explore()
  hrefs = []
  for section in range(1,8):
    for post in range(1,5):
      # Each post on explore page
      element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[{section}]/div[{post}]"))))
      action = ActionChains(browser)
      action.move_to_element(element).click().perform()
      # Like buttons on posts
      element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a"))))
      hrefs.append(element.get_attribute("href"))
      # # Person list that likes the post
      # for persons in range(70):
      #   element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div"))))
      #   element.click()
      #   for tabs in range(3):
      #     element.send_keys(Keys.TAB)

      #   element = browser.switch_to.active_element()
      #   print(element.text)

      # Exit button of the posts
      element = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div"))))
      element.click()
  # Go to href of the likes
  for href in range(len(hrefs)):
    print(len(hrefs))
    browser.get(hrefs[href])
    for person in range(1,30):
      # Get the button text
      element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div/div[{person}]/div[3]/button/div/div"))))
      # if not following the person already follow
      if(element.text == "Takip Et"):
        print("followed")
        element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,(f"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div/div[{person}]/div[3]/button"))))
        element.click()
        sleep(1)
      else:
        pass 
    sleep(3)


follow_from_explore()