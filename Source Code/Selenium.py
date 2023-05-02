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

def login(driver, username, password):
    driver.get("https://newbuildhomes.org/wp-login.php")
    username_elem = driver.find_element(By.ID, "user_login")
    password_elem = driver.find_element(By.ID, "user_pass")
    login_button = driver.find_element(By.ID, "wp-submit")
    username_elem.send_keys(username)
    password_elem.send_keys(password)
    login_button.click()
    print("Login Successful")
    for i in range(3):
        post_id = 24732 + i*2
        url = f"https://newbuildhomes.org/wp-admin/post.php?post={post_id}&action=edit"
        print(url)
        driver.get(url)
        print(f"Opened post {post_id}")
    

def upload_media(driver, media):
    
    media_tab = driver.find_element(By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[4]/a')
    media_tab.click()
    time.sleep(2)
    for image in media:
        wait = WebDriverWait(driver, 10)
        # backdrop = wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, '.media-modal-backdrop')))
        add_media_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/div/div[4]/div[1]/div/div/div[2]/div/div[2]/a')))
        time.sleep(3)
        add_media_button.click()
        time.sleep(2)
        upload_file_button = driver.find_elements(By.CSS_SELECTOR, '#menu-item-upload')[-1]
        upload_file_button.click()
        time.sleep(2)
        select_files_button = driver.find_elements(By.CSS_SELECTOR, '.wp-core-ui .button-group.button-hero .button, .wp-core-ui .button.button-hero')[-1]
        select_files_button.click()
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", image)
        time.sleep(1)
        autoit.control_send("Open", "Edit1", "{ENTER}")
        time.sleep(7)
        select_button = driver.find_elements(By.XPATH, '//button[@class="button media-button button-primary button-large media-button-select"]')[-1]
        if select_button.is_enabled():
            select_button.click()
        else:
            time.sleep(10)
            select_button.click()
        time.sleep(5)
    # update_button = driver.find_element(By.ID, "publish")
    # update_button.click()

    print("Media Uploaded")

def update_price(driver, primary_price, secondary_price):
    wait = WebDriverWait(driver, 10)
    info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[1]/a')))
    # wait.until(EC.invisibility_of_element_located((By.XPATH, '//a[@href="https://newbuildhomes.org/"]')))
    info.click()

    enter_price = driver.find_element(By.ID, 'fave_property_price')
    enter_price.clear()
    time.sleep(2)
    enter_price.send_keys(str(primary_price))
    print("Enter primary price:", primary_price)
  
    enter_2price = driver.find_element(By.ID, 'fave_property_sec_price')
    enter_2price.clear()
    enter_2price.send_keys(str(secondary_price))
    print("Enter secondary price:", secondary_price)
    time.sleep(1)
    update_button = driver.find_element(By.ID, "publish")
    update_button.click()
    time.sleep(1)
    print("Price Updated")

def main():
    service = Service("C:/Drivers/chromedriver.exe")
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome(service=service, options=options)
    driver.implicitly_wait(0.5)

    # Login
    username = "Muktesh"
    password = "2d6cHuKWGAxU0OOpHJ4yrsem"
    login(driver, username, password)

    # Upload media
    wb = openpyxl.load_workbook('Property.xlsx')
    ws = wb['extraction results']
    for row in ws.iter_rows(min_row=2, max_row=4, min_col=1, values_only=True):
        media = row[5].replace("]", "").replace("[", "").replace("'", "").replace("/","\\").split(",")
        upload_media(driver, media)
    #update Price
        price = row[4]
        primary_price = int(re.search("£([\d,]+)", price).group(1).replace(",", ""))
        secondary_price_match = re.search("- £([\d,]+)", price)
        secondary_price = int(secondary_price_match.group(1).replace(",", "")) if secondary_price_match else ('')
       
        update_price(driver, primary_price, secondary_price)

    driver.quit()

if __name__ == "__main__":
    main()