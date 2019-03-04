import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 

print(config.WEBSITE_URL)
chrome_options = Options()  
#chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)

buy_order = '10'

def BuyMethod(driver,buy_order,config):
    driver.get(config.WEBSITE_URL)
    user_name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    # sends keys to login
    user_name.send_keys(config.USERNAME)
    password.send_keys(config.PASSWORD)

    # clicks the log in button
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/form/footer/div/button').click()


    # clicks on the first symbol we also need to wait.
    click_ele = WebDriverWait(driver,15).until(
    lambda x: x.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/section[2]/a[1]')
    )
   
    click_ele.click()

    buy_form = WebDriverWait(driver,15).until(
    lambda x:  x.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div/div/main/div[2]/div[2]/div/form/div[1]/div[1]/div[1]/label/div[2]/input'))

    buy_form.send_keys(buy_order)

    review_button = WebDriverWait(driver,30).until(
    lambda x: x.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div/div/main/div[2]/div[2]/div/form/div[1]/div[3]/div/div[2]/button')
    )
    review_button.click()




   
    buy_button = WebDriverWait(driver,30).until(
        lambda x: x.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div/div/main/div[2]/div[2]/div/form/div[1]/div[3]/div/div[2]/button[1]').click()
    )

    driver.close()

BuyMethod(driver,buy_order,config)
