import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

if __name__ == '__main__':

    browser = webdriver.Chrome()
    browser.get('https://yoursite.com/login')

    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
        cookie['domain'] = ".application.daffodilvarsity.edu.bd"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    time.sleep(2)
    browser.get("https://yoursite.com/dashboard")

    time.sleep(2)
    browser.get("https://yoursite.com/profile")
    name =  browser.find_element(By.NAME, 'name').get_attribute("value")
    print(name)

    time.sleep(120)