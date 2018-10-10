####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
# Not always used for every test
###################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from datetime import datetime
from time import sleep
from reusableFxns import *

###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs Tests
###################################################################
sauceParameters = {
    'tags':['Case', 'NUM',],
    'platform': 'Windows 10',
    'browserName': 'chrome',
    'version': 'latest',
    'screenResolution':'1920x1080',
    'name': 'Run: ' + getNumber(),
    #'tunnelIdentifier':'Phill Tunnel One',
    #'seleniumVersion': '3.8.1',
    #'ieDriverVersion': '3.4.0',
    #'chromedriverVersion': '2.40',
    #'requireWindowFocus' : True,
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

#interact = driver.find_element_by_class_name('figure')
#sleep(10)
#print('Message')
#ActionChains(driver).move_to_element(interact).perform()

#driver.save_screenshot('screenshot.png')
#interact.send_keys('Dryzz')
#interact.submit()
#driver.execute_script('sauce: break')
#driver.execute_script('sauce:context=Place words here for notes')

driver.quit()

