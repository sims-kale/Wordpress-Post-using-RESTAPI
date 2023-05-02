import re
import openpyxl
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import time

service = Service("C:/Drivers/chromedriver.exe")
options = ChromeOptions()
# options.add_argument("Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL25ld2J1aWxkaG9tZXMub3JnIiwiaWF0IjoxNjgyNjEzMDIzLCJuYmYiOjE2ODI2MTMwMjMsImV4cCI6MTY4MzIxNzgyMywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.HeZIB0CKWhhPcsFPAZAeiSbcQQff55NeBcIN7plmJGQ")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Chrome(service=service, options=options)
driver.implicitly_wait(0.5)
driver.get("https://newbuildhomes.org/wp-admin/post.php?post=24600&action=edit")

username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID, "user_pass")
login_button = driver.find_element(By.ID, "wp-submit")
username.send_keys("Muktesh")
password.send_keys("2d6cHuKWGAxU0OOpHJ4yrsem")
login_button.click()
print("Login Successful")

wb = openpyxl.load_workbook('Property.xlsx')
ws = wb['extraction results']
for row in ws.iter_rows(min_row=4, max_row=4, min_col=1, values_only=True):
    price = row[4]
    print(price)
    primary_price = int(re.search("£([\d,]+)", price).group(1).replace(",", ""))
    secondary_price_match = re.search("- £([\d,]+)", price)
    secondary_price = int(secondary_price_match.group(1).replace(",", "")) if secondary_price_match else ('')
    

    
    enter_price = driver.find_element(By.ID, 'fave_property_price')
    enter_price.clear()
    enter_price.send_keys(str(primary_price))
    print("Enter primary price:", primary_price)

    enter_2price=driver.find_element(By.ID, 'fave_property_sec_price')
    enter_2price.clear()
    enter_2price.send_keys(str(secondary_price))
    print("Enter secondary price:", secondary_price)
    time.sleep(5)
   
    update_button = driver.find_element(By.ID, "publish").click()
    time.sleep(10)

    print("Post Updated")
    driver.quit()
