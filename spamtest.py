#Imports the webdriver component of selenium, used for automated web scraping. Documentation here http://www.seleniumhq.org/docs/03_webdriver.jsp
from selenium import webdriver
 
#Creates a driver that we use to control the browser. This line is where you see the chrome window open

from time import sleep
"""
#if you are using bash, use the commented out version of the path but replace natek and on with your file location
#driver = webdriver.Chrome("/mnt/c/Users/natek/Documents/Python Test Spam/chromedriver.exe")

"""

"Otherwise if you are using anaconda in a windows environment use this"
driver = webdriver.Chrome("chromedriver.exe") 
#We open the correct webpage. Equivelant to pasting the url into the omnibox and pressing enter.
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSexgwjLLgUSYUMQmZhArCNsbBiVTc7FMoXYIbUIMpmMAH8jdg/viewform")


while True:
    #This line is quite complicated. The radial button doesn't actually have a clickable element, and instead uses javascript for form control.
    #Because of this the standard method of clicking in selenium won't work. Instead we use actionchains, which allows us to take direct control of the mouse.
    #We instruct it to move to the element we want to click, which we locate by xpath. We then tell it to click and finally we call perform so the action chain is executed.
    
    #webdriver.ActionChains(driver).move_to_element(driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div/div[2]/div/content/div/label[6]/div/div/div[3]/div")).click().perform()
    driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div/div[2]/div/content/div/label[6]/div/div/div[3]/div").click()
    #Here we can use the standard way of clicking, since the actual vote button itself is clickable. We locate the vote button by xpath and click it.
    driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div/content/span").click()
 
    #This is so it accidentally doesn't 
    sleep(.1)
    driver.find_element_by_css_selector("a").click()
    