from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Webdriverwait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.chrome()

driver.get('https://www.google.com/')

#explicit Driver waiting Time
driver.maximize_window()

bt_1=driver.find_element_by('q')
# according to echange the name of class in the web pages we use Xpath to find the Page and Box for entering Data
bt2=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]").click()
# CSS Selector 
bt2=driver.find_element_by_css_selector('css selector Code').click

bt_1.send_keys('python'+Keys.ENTER)  # write python in search box of google and press Enter Button
time.sleep(3)

# implicit Driver Waiting Time 
# it can be used with Xpath instaid
bt1=Webdriverwait(driver,10).until(EC.element_to_be_clickable(By.NAME,'q'))
bt_1.send_keys('python')
bt_1.click()






