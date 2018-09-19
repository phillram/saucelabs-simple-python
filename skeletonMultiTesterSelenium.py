####################################################################
# Skeleton for Multi Testing Selenium tests on Sauce Labs
####################################################################


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
import multiprocessing
from reusableFxns import *


###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################

run = 30

###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Sauce Labs Tests
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
    # Connect to Sauce Labs
    ###################################################################
    driver = webdriver.Remote(
        command_executor='http://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities=sauceParameters)
    
    ###################################################################
    # Test logic goes here
    ###################################################################
    driver.get('https://www.dryzz.com')

    interact = driver.find_element_by_id('menu-item-112')
    interact.click()

    #driver.save_screenshot('screenshot.png')
    #interact.send_keys('Dryzz')
    #interact.submit()
    #driver.execute_script('sauce: break')
    #driver.execute_script('sauce:context=Place words here for notes')
    driver.quit()


###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################

if __name__ == '__main__':
    jobs = [] #Array for the jobs
    for i in range(run): # Run the amount of times set above
        p = multiprocessing.Process(target=run_sauce_test) #Define what function to run multiple times.
        jobs.append(p) # Add to the array.
        p.start() #Start the functions.
        #print('this is the run for: '+ str(i))

