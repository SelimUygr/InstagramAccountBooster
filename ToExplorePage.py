from Login import WebDriverWait,By,EC,TimeoutException,login,login


def to_explore():
  #Explore button
  try:
    browser = login()
    element = WebDriverWait(browser,150).until(EC.presence_of_element_located((By.XPATH,("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/a/div"))))
    element.click()
    #Click on first Post 
    # Will get this inside for loop
    return browser
  except TimeoutException:
    print("Error while trying to go to explore page!\n Please make sure explore button is visible.")
