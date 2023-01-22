from selenium import webdriver




def configure_browser():
  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach",True)
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()
  return browser
  

