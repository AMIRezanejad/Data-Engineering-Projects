from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Webdriverwait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
import time

#  Building a Bot and the way of compliting the Psychology test via Bot which we have been built

driver=webdriver.chrome()

driver.get('https://www.google.com/')

#explicit Driver waiting Time
driver.maximize_window()


waits=Webdriverwait(driver,20) # building an Object for runing page and implicitly waiting for Loadig the page
#We will use X_number for Each step of click or selecting a value of box
x_1=waits.until(EC.element_to_be_clickable(By.NAME,'q')) # 
x_1.send_keys('psychology Test'+Keys.ENTER)  # write python in search box of google and press Enter Button

# after searching Google web page and finding the Psychology test
# we will find the CSS selector of item which is found
x_2=waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'css selector Codeof psychology web page').click()

# finding the link text of Psycological Test in Web Page
x_3=waits.until(EC.element_to_be_clickable((By.LINK_TEXT,'text link of Test on page '))).click()
x_4=waits.until(EC.element_to_be_clickable((By.Xpath,'Xpath link'))).click()
# select male in dropbox of sex
x_5=waits.until(EC.element_to_be_clickable((By.Xpath,'//select[@name='sex']')))
drop_1=select(x_5)
drop1.selct_by_value('male') 

# select birthday from Dopbox
x_6=waits.until(EC.element_to_be_clickable((By.ID,'year_birth')))
drop_1=select(x_6)
drop1.selct_by_value('1365') 

#press start Test Buttom
x_7=waits.until(EC.element_to_be_clickable((By.Xpath,'//buttom[@Type='submit']'))).click()

# DOING TEST
i=1

while i<=10 :
    if i==1:   # question 1
        x8=waits.until(EC.element_to_be_clickable((By.Xpath,'//label[@for='answer_1']'))).click()  
    elif i==2: #question 2
        x9=waits.until(EC.element_to_be_clickable((By.Xpath,'//label[@for='answer_2']'))).click() 
    i+=1



        




