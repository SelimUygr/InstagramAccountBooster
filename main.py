from ToExplorePage import to_explore,WebDriverWait,By,EC,TimeoutException,sleep

def follow_from_explore_page():
  browser = to_explore()
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

follow_from_explore_page()

  