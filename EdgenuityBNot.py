import selenium
from selenium import webdriver
import time
# Important note about the use of time.sleep() -
# I am using it as a buffer so the program doesnt try to click an element that doesn't exist.
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\Noah Linton\Downloads\New folder\geckodriver.exe')
driver.get("https://auth.edgenuity.com/Login/Login/Student")
# Getting Username Field
username = driver.find_element_by_id("LoginUsername")
username.send_keys("s12236717duval")
# Getting Password Field
password = driver.find_element_by_id("LoginPassword")
password.send_keys("password")
# Proceeding to main site
login = driver.find_element_by_id('LoginSubmit')
login.click()
time.sleep(3)
try:
    continuebutton = driver.find_element_by_id("btnContinue")
finally:
    continuebutton.click()
# Going into Economics Section
time.sleep(1)
driver.get("https://r06.core.learn.edgenuity.com/Student/activities/coursemap.aspx?StudentBuildID=94290235")
# economicssections = driver.find_element_by_id("94290235")
# economicssections.click()
# Navigating the pages

# Intro To Economics Section of Edgenuity
#ids = driver.find_elements_by_xpath('//*[@id]')
#for ii in ids:
    #print ii.tag_name
 #   print(ii.get_attribute('id'))  # id name as string


