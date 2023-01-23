import os
from dotenv import load_dotenv,find_dotenv


#Loading .env file
load_dotenv()
#Get username-password from .env
def get_username():
  username =os.getenv("IG_USERNAME")
  return username
def get_password():
  password = os.getenv("IG_PASSWORD")
  return password