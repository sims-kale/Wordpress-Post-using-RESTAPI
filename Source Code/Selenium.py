import logging
import re
import openpyxl
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
import time
import autoit

logging.basicConfig(filename='Source Code/Selenium.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def login(driver, username, password):
    driver.get("https://newbuildhomes.org/wp-login.php")
    username_elem = driver.find_element(By.ID, "user_login")
    password_elem = driver.find_element(By.ID, "user_pass")
    login_button = driver.find_element(By.ID, "wp-submit")
    username_elem.send_keys(username)
    password_elem.send_keys(password)
    login_button.click()
    logging.info("Login Successful")
    
    

def upload_media(driver, media):
    if media == ['']:
        logging.info("Media is not available. Skiping..")
        return None
    
    media_tab = driver.find_element(By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[4]/a')
    time.sleep(2)
    media_tab.click()
    print('length of media', len(media), '\n')
    for image in media:
        new_name = image.replace(" by", '').replace(" in", '').strip()
        rename= new_name.replace(" ", "-").replace("'","")
        print('Image Path-',rename,'\n')  #update Media
        logging.info("Image Path: " + rename)
        wait = WebDriverWait(driver, 7)
        # backdrop = wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, '.media-modal-backdrop')))
        add_media_button = driver.find_elements(By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/div/div[4]/div[1]/div/div/div[2]/div/div[2]/a')[0]
        # driver.execute_script("arguments[0].click();", add_media_button)
        add_media_button.click()
        time.sleep(2)
        upload_file_button = driver.find_elements(By.CSS_SELECTOR, '#menu-item-upload')[-1]
        upload_file_button.click()
        time.sleep(2)
        select_files_button = driver.find_elements(By.CSS_SELECTOR, '.wp-core-ui .button-group.button-hero .button, .wp-core-ui .button.button-hero')[-1]
        select_files_button.click()
        autoit.win_wait_active("Open")
        time.sleep(5)
        autoit.control_set_text ("Open", "Edit1", rename)
                                                    # 'C:\Users\Administrator\Desktop\URLS_sCRAPPING\Images\Chap-at-Countesswells-Aberdeen-CHAP-Homes1.jpg'
                        # Hazelwood-Aberdeen-Dandara1.jpg
        autoit.control_send("Open", "Edit1", "{ENTER}")
        time.sleep(5)
        select_button = driver.find_elements(By.XPATH, '//button[@class="button media-button button-primary button-large media-button-select"]')[-1]
        if select_button.is_enabled():
            time.sleep(3)
            select_button.click()
        else:
            time.sleep(30)
            select_button.click()
    logging.info("Media Uploaded")
    time.sleep(10)

def update_price(driver, price, primary_price, secondary_price):
    if price is None:
        logging.info("Prices are None, skipping...")
        return None
    logging.info("Prices: " + price)
    wait = WebDriverWait(driver, 60)
    info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[1]/a')))
    driver.execute_script("arguments[0].scrollIntoView();", info)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
    info.click()
    time.sleep(3)
    enter_price = driver.find_element(By.ID, 'fave_property_price')
    enter_price.clear()

    enter_price.send_keys(str(primary_price))
    logging.info("Enter primary price:" + str(primary_price))
  
    enter_2price = driver.find_element(By.ID, 'fave_property_sec_price')
    enter_2price.clear()
    enter_2price.send_keys(str(secondary_price))
    logging.info("Enter secondary price:" +  str(secondary_price))
    time.sleep(5)
    logging.info("Price Updated")

def developer(driver, dev_names):
    if dev_names is None:
        logging.info("Developer names is None, skipping...")
        return None
    logging.info("Developer Names: " + dev_names)
    wait = WebDriverWait(driver, 60)
    info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="houzez-property-meta-box"]/div[2]/div/div/ul/li[1]/a')))
    driver.execute_script("arguments[0].scrollIntoView();", info)
    wait = WebDriverWait(driver, 20)
    contact_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li[6]/a')))
    # contact_button = wait.until(EC.element_to_be_clickable((By.XPATH,  '/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li[6]/a')))          
    driver.execute_script("arguments[0].click();",contact_button)       
    time.sleep(10)
    contact_button.click()
    time.sleep(2)
    radio_button= wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[6]/div[1]/div/div/div[2]/ul/li[3]/label/input')))
    # radio_button= wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[6]/div[1]/div/div/div[2]/ul/li[3]/label/input')))
                                                                            
    radio_button.click()
    time.sleep(2)
    input= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[6]/div[3]/div/div/div[2]/span/span[1]/span/span[1]/span')))
    # input= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[6]/div[3]/div/div/div[2]/span/span[1]/span/span[1]/span')))
                                                                                                                       
    input.click()
    time.sleep(2)   
    serach_field= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
    serach_field.click()
    time.sleep(3)                                     
    serach_field.send_keys(dev_names)
    slelect_result= driver.find_element(By.XPATH, '//*[@id="select2-fave_property_agency-results"]')
    time.sleep(5)
    slelect_result.click() 
    time.sleep(5)

def Map(driver, zipcode):
        wait = WebDriverWait(driver, 15)
        map_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li[2]/a')))
        time.sleep(10)
        map_button.click()
        input= driver.find_element(By.XPATH, '//*[@id="fave_property_map_address"]')
        time.sleep(2)
        input.click()
        input.clear()
        input.send_keys(zipcode)
        time.sleep(3)
        select_field= driver.find_element(By.XPATH,'//ul[@class="ui-menu ui-widget ui-widget-content ui-autocomplete ui-front"]')
        time.sleep(2)
        option= select_field.find_element(By.XPATH,'.//li')
        time.sleep(2)
        option.click()    
        time.sleep(2)  
# Property Setting
def Address(driver, address, zipcode):
    if address is None:
        logging.info("Address is None, skipping...")
        return None
    
    else:
        wait = WebDriverWait(driver, 10)                                                                                                               
        adress_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li[3]/a')))
        adress_button.click() 
        time.sleep(2)

        street= driver.find_element(By.XPATH,'//*[@id="fave_property_address"]')
        time.sleep(3)
        street.click()
        street.clear()
        street.send_keys(address)
        time.sleep(2)
        zip=driver.find_element(By.XPATH,'//*[@id="fave_property_zip"]')
        time.sleep(2)
        zip.click()
        zip.clear()
        zip.send_keys(zipcode)
        time.sleep(2)

        logging.info("Address updated")

def main():
    
    service = Service("C:/Drivers/chromedriver.exe")
    options = ChromeOptions()
    # options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome(service=service, options=options)
    # driver.maximize_window()
    driver.implicitly_wait(0.5)

    # Login
    username = "Muktesh"
    password = "2d6cHuKWGAxU0OOpHJ4yrsem"
    login(driver, username, password)

                                                                                                            
    wb = openpyxl.load_workbook('Property.xlsx')                                                         # Upload media
    ws = wb['extraction results']
    for row in ws.iter_rows(min_row=2385, max_row=2400, min_col=1, values_only=True):
        
        mediaCell=row[5]
        media = row[5].replace("]", "").replace("[", "").replace("/","\\").split(",")[:50]
    
        print('media', media, '\n')
        
        property_update_url = row[7]
        print('property url', property_update_url, '\n')
        #
        logging.info("update URL: " +property_update_url)
        
        driver.get(property_update_url)
        upload_media(driver, media)
        price = row[4]
        if price is None:
            logging.info("price is None, skipping...")
            pass                                                                 #update Media
        else:    
                                                                                  #update Media
            # primary_price = int(re.search("£([\d,]+)", price).group(1).replace(",", ""))
            # secondary_price_match = re.search("- £([\d,]+)", price)
            # secondary_price = int(secondary_price_match.group(1).replace(",", "")) if secondary_price_match else ('')
            if 'From' not in price:

                primary_price = price.split('-')[0].replace('£','').replace(',','').strip()
                secondary_price = price.split('-')[1].replace('£','').replace(',','').strip()
            else:
                primary_price = price.split(' ')[1].replace('£','').replace(',','').strip()
                secondary_price = ''
            

            print('primary price', primary_price, '\n')
            print('secondary price', secondary_price, '\n')
            update_price(driver,price, primary_price, secondary_price)
        # element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li[6]/a')
        dev_names= row[1].split("by")[1]                                                                  #Update Developer
        developer(driver, dev_names)
        address = row[2]
        
        if address is None:
            logging.info("Address is None, skipping...")
            pass
    
        else:
            zipcode = row[2].split(",")[-1] 
            Address(driver, address, zipcode)
            if zipcode == "":
                logging.info("zipcode is None, skipping...")
                pass                    
            else:
                Map(driver, zipcode)
                
        logging.info("Address"+ address)

        update_button = driver.find_element(By.ID, "publish")
        time.sleep(5)
        update_button.click()
        time.sleep(10)
        logging.info("Post Updated !")
        logging.info("-----------------------------------------------------------------------------")
    driver.quit()

if __name__ == "__main__":
    main()