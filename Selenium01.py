#call selenium
#use selenium commands

#Selenium code(Python,Java) --> API HTTP Request --> chrome/Gecko Driver --> Chrome/FireFox

from selenium import webdriver

#create the session
#send the commands
#if we are using selenium <4 , we use to set the driver path
#if we are using selenium >4 , Driver path is not needed , they will handle automatically

browser = webdriver.Chrome()
browser.get("https://app.vwo.com")

