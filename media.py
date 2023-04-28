from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Launch a browser
service = Service("C:/Drivers/chromedriver.exe")
options = ChromeOptions()
# options.add_argument("Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL25ld2J1aWxkaG9tZXMub3JnIiwiaWF0IjoxNjgyNjEzMDIzLCJuYmYiOjE2ODI2MTMwMjMsImV4cCI6MTY4MzIxNzgyMywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.HeZIB0CKWhhPcsFPAZAeiSbcQQff55NeBcIN7plmJGQ")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Chrome(service=service, options=options)


driver.implicitly_wait(0.5)

# driver.get("https://newbuildhomes.org/wp-login.php")
driver.get("https://newbuildhomes.org/wp-admin/post.php?post=20610&action=edit")

# Log in to WordPress
username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID,"user_pass")
login_button = driver.find_element(By.ID,"wp-submit")

username.send_keys("Muktesh")
password.send_keys("2d6cHuKWGAxU0OOpHJ4yrsem")
login_button.click()
print("Login Successful")

# Navigate to the media library
media_library_link = driver.find_element(By.CSS_SELECTOR,'.wp-core-ui')
media_library_link.click()
print("Adding Media")

media_library_link.send_keys("D:/Relu/Wordpress data/images/1.1.jpeg")
print("Media Uploaded")

time.sleep(30)

insert_button = driver.find_element(By.CSS_SELECTOR,".wp-core-ui .button.button-large")
insert_button.click()
print("Inserted")

# Log out of WordPress
# logout_link = driver.find_element_by_xpath("//a[contains(text(),'Log Out')]")
# logout_link.click()

driver.quit()
