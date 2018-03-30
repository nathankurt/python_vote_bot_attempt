#!/usr/bin/env python3

#making this a script so you can enter args for how many times you want to run it.


#Imports the webdriver component of selenium, used for automated web scraping. Documentation here http://www.seleniumhq.org/docs/03_webdriver.jsp
from selenium import webdriver
 
#Creates a driver that we use to control the browser. This line is where you see the chrome window open

from time import sleep

import sys, os


"""TODO: I'm not sure if making a function for submitting would be faster so i may play around with it."""

#checking if the user inputted system arguments, if they didn't then make it an infinite loop. 
if(len(sys.argv) == 1):
    #means they didn't enter a value for argument. You can yell or default. I think i'm going to just make it infite if no args.
    run_times = 25000
elif(len(sys.argv) > 2):
    #Entered too many arguments
    print("ERROR: INVALID NUMBER OF ARGS")
else:
    #1 arg so set that as amount of times
    try:
        #checks to see that they entered a number value for the script argument
        run_times = int(sys.argv[1])
    except ValueError:
        print("ERROR: INVALID ARGUMENT")



#Use this to get the path of the chromedriver webdriver that's in the same folder as your script.
path = os.path.abspath("chromedriver.exe")

driver = webdriver.Chrome(path) 
#We open the correct webpage. Equivelant to pasting the url into the omnibox and pressing enter.
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSexgwjLLgUSYUMQmZhArCNsbBiVTc7FMoXYIbUIMpmMAH8jdg/viewform")

# Use a generator like suggested here to do a while loop in a for loop. "https://stackoverflow.com/questions/34253996/infinite-for-loops-possible-in-python"
for n in range(run_times):
   
    #Here we can use the standard way of clicking, since the actual vote button itself is clickable. We locate the vote button by xpath and click it.
    driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div/div[2]/div/content/div/label[6]/div/div/div[3]/div").click()
    #Here we can use the standard way of clicking, since the actual vote button itself is clickable. We locate the vote button by xpath and click it.
    driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div/content/span").click()
 
    #This is so it accidentally doesn't click on the wrong thing.
    sleep(.1)

    #click the submit again button
    driver.find_element_by_css_selector("a").click()



