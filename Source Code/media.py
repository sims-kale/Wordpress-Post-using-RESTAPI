from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import time

# Launch a browser
service = Service("C:/Drivers/chromedriver.exe")
options = ChromeOptions()
# options.add_argument("Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL25ld2J1aWxkaG9tZXMub3JnIiwiaWF0IjoxNjgyNjEzMDIzLCJuYmYiOjE2ODI2MTMwMjMsImV4cCI6MTY4MzIxNzgyMywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.HeZIB0CKWhhPcsFPAZAeiSbcQQff55NeBcIN7plmJGQ")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Chrome(service=service, options=options)


driver.implicitly_wait(0.5)

# driver.get("https://newbuildhomes.org/wp-login.php")
driver.get("https://newbuildhomes.org/wp-admin/post.php?post=24600&action=edit")

# Log in to WordPress
username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID,"user_pass")
login_button = driver.find_element(By.ID,"wp-submit")

username.send_keys("Muktesh")
password.send_keys("2d6cHuKWGAxU0OOpHJ4yrsem")
login_button.click()
print("Login Successful")



# USING FILE PATH
media_field= driver.find_element(By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[4]/a').click()
print("Media filed Clicked")
Add_Media= driver.find_element(By.CSS_SELECTOR,'#houzez-property-meta-box > div.inside > div > div > div > div.rwmb-tab-panel.rwmb-tab-panel-gallery > div:nth-child(1) > div > div > div.rwmb-input > div > div.rwmb-media-add > a').click()


print("Add Media Button")


upload_file=driver.find_element(By.CSS_SELECTOR,"#menu-item-upload").click()

print("Clicked on upload files")


Select_files= driver.find_element(By.CSS_SELECTOR,'.wp-core-ui .button-group.button-hero .button, .wp-core-ui .button.button-hero').click()

print("Select file")

autoit.win_wait_active("Open")
autoit.control_set_text("Open","Edit1", r"D:\relu\Wordpress data\property_images\1 Creekside in Deptford by Lewisham Homes1.jpg")
autoit.control_send("Open", "Edit1", "{ENTER}")

select_button = driver.find_elements(By.XPATH,'//button[@class="button media-button button-primary button-large media-button-select"]')[-1]

time.sleep(5)
select_button.click()
# print(len(select_button))
# last_button = select_button[-1] # select the last button in the list
# print(last_button)
# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(last_button).click(last_button).perform()
print("file Uploaded")
time.sleep(5)

update_button=driver.find_element(By.ID, "publish").click()
time.sleep(10)

print("Post Updated")



driver.quit()
