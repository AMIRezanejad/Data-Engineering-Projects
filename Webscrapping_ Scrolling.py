from selenium import webdriver

#  Building a Bot and the way of compliting the Psychology test via Bot which we have been built

driver=webdriver.chrome()

driver.get('https://lenz.varzesh3.com/')

#explicit Driver waiting Time
driver.maximize_window()

# scrolling method 
# it will scroll till 

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep()
    my_scroll= driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        break
    end_of_scroll=my_scroll


# extract all the comments in the page
text=driver.find_elements_by_css_selector('css selector Code for extract all the comments in the page  for example :span.text ')
for f in text:
    print(t.text)

