import json
import request
import jsonpath
import pytest
from selenium import webdriver

driver = webdriver.chrome(executable_path='/home/manikandan/Documents/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.google.com')

assert 'google' in driver.current_url