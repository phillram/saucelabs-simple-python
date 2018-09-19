###################################################################
#This is a list of easy to copy and to use functions that I found
#over the support time
###################################################################



###################################################################
# Imports that are good to use
###################################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
from datetime import datetime
from time import sleep


###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs tests
###################################################################

sauceParameters = {
    'tags':['Case', '11111',],
    'platform': 'Windows 10',
    'browserName': 'chrome',
    'version': 'latest',
    'screenResolution':'1920x1080',
    'name': 'Run: ' + getNumber(),
    #'seleniumVersion': '3.8.1',
    #'iedriverVersion': '3.4.0',
    #'maxDuration': 1800,
    #'idleTimeout': 1000,
    #'commandTimeout': 600,
    #'videoUploadOnPass':False,
    #'extendedDebugging':'true',
    #'prerun':{ 
        #'executable': 'https://gist.githubusercontent.com/phillram/92a0f22db47892e4b27d04066084ce92/raw/aaeee222780e4ad8647667b267d81684d6059b5c/set_agent.sh',
        #'args': '',
        #'background': 'true',
    #},
    #'chromeOptions':{
        #mobileEmulation':{'deviceName':'iPhone X'}
    # },
}

# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

###################################################################
#Connect to Sauce Labs using OS environment variables
###################################################################
driver = webdriver.Remote(
    command_executor='http://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:80/wd/hub',
    desired_capabilities=sauceParameters)

driver = webdriver.Remote(
    command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
    desired_capabilities=sauceParameters)



###################################################################
#This will search for an element. If it doesn't find the element (gets an exception)
#Tthen it will perform a task.
#It loops until there is no exception (break)
###################################################################
driver.get('https://www.dryzz.com')
while True:
    try: #Try to do the below
        driver.find_element_by_link_text('Projects')
        break #If element found then break out of while loop
    except: #perform these actions if there is an exception
        interact = driver.find_element_by_name('username')
        interact.send_keys('test_user_mcgoo')
        interact = driver.find_element_by_name('password')
        interact.send_keys('test_user_mcgoo')
        interact.submit()

###################################################################
#Set a breakpoint in your test
#This will stop the test at this point and allow manual
#control on the Sauce Labs website
###################################################################
driver.execute_script('sauce: break')

###################################################################
#This adds notes to the command window in Sauce Labs dashboard
###################################################################
driver.execute_script('sauce:context=Place words here for notes')

###################################################################
#Take screenshot
###################################################################
driver.save_screenshot('screenshot.png')

###################################################################
# Mark a test pass or failed in execution
###################################################################
driver.execute_script('sauce: job-result=passed')
driver.execute_script('sauce: job-result=failed')


###################################################################
# This opens a file to increment the number
###################################################################
def getNumber(filename='countFile.txt'):
    with open(filename, 'r+') as f:
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        f.close()
        #print ('This is test Run: ' + str(val))
        return str(val)



###################################################################
#Stop test
###################################################################
driver.quit()

