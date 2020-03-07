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
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'

###################################################################
# Common parameters (desired capabilities)
###################################################################
sauceParameters = {
    'tags':['Case', 'NUM',],
    'name': 'Run: ' + getNumber(),
    'platform': 'Windows 10',
    'browserName': 'chrome',
    # The following are not required
    # 'version': 'latest',
    # 'screenResolution':'1920x1080',
    # 'seleniumVersion': '3.141.59',

    # Sauce Specific Options
    # 'extendedDebugging': 'true',
    # 'capturePerformance': 'true',
    # 'idleTimeout': 180,
    # 'commandTimeout': 600,
    # 'prerun':{
    #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
    #     'args': ['--silent'],
    #     'timeout': 500,
    #     'background': 'false',
    # },

    # Browser Specific Options        
    # 'chromeOptions':{
    #     'mobileEmulation':{'deviceName':'iPhone X'},
    #     'prefs': {
    #         'profile': {
    #             'password_manager_enabled': 'false',
    #             },
    #             'credentials_enable_service': 'false',
    #         },
    #     'args': ['test-type', 'disable-infobars'],
    # },

    # 'moz:firefoxOptions':{
    #     'log': {'level': "trace"},
    # },
}
# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print("You are using the US data center")
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print ("You are using the EU data center")
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
#__________________________________________________________________
driver.get('https://www.dryzz.com')

# Setup for finding an element and clicking it
#__________________________________________________________________
interact = driver.find_element_by_id('menu-item-112')
interact.click()

# Setup for finding an element and sending keystrokes
#__________________________________________________________________
# interact = driver.find_element_by_class_name('figure')
# interact.send_keys('Dryzz')
# interact.submit()

# Setup for using random Python commands
#__________________________________________________________________
# driver.save_screenshot('screenshot.png')
# sleep(10)
# print('Message')

# Setup for using Action chains
#__________________________________________________________________
# ActionChains(driver).move_to_element(interact).perform()

# Setup for random script executions
#__________________________________________________________________
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Place words here for notes')

# Ending the test session
#__________________________________________________________________
driver.quit()
