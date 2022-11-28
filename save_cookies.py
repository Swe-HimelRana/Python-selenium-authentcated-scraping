import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    email = "username"
    password = "password"

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    browser = webdriver.Chrome(
        options=options,
    )
    browser.get('https://yoursite.com/login')
    time.sleep(5)

    browser.find_element(By.ID, 'email').send_keys(email)
    browser.find_element(By.ID, 'password').send_keys(password)

    browser.find_element(
        By.XPATH, '/html/body/div[1]/div/div/form/div[3]/button').click()

    time.sleep(5)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))

