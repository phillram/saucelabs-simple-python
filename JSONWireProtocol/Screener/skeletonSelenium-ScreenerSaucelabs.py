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
# Common parameters (desired capabilities)
###################################################################
screenerParameters = {
    # These Screener capablities are required. You'll find the apiKey and group name in the Screener.io dashboard
    # Using the proxy flag will have the tests run on Sauce Labs cloud with your Sauce Labs credentials
    # This proxy will likely no longer be necessary when Screener is integrated into Sauce
    'screener': {
        'apiKey': os.environ['SCREENER_API_KEY'],
        'group': os.environ['SCREENER_GROUP_KEY'],
        'name': 'Visual Test',
        'resolution': '1920x1080',
        'proxy': 'https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com/wd/hub',
        # 'proxy': 'https://' + os.environ['SAUCE_USERNAME'] + ':' + os.environ['SAUCE_ACCESS_KEY'] + '@ondemand.eu-central-1.saucelabs.com',
    },

    # Sauce Specific Options
    'tags':['Screener', 'Tests',],
    'name': 'Run: ' + getNumber(),
    'platform': 'Windows 10',
    'browserName': 'chrome',
    'screenResolution':'1920x1080',
    # The following are not required
    # 'version': 'latest',
    # 'seleniumVersion': '3.141.59',
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
screenerParameters.update({'build': '-'.join(screenerParameters.get('tags'))})

###################################################################
# Connect to Screener
###################################################################
driver = webdriver.Remote(
    command_executor='https://hub.screener.io/wd/hub',
    desired_capabilities=screenerParameters)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
driver.get('https://www.google.com')

# Taking a screenshot on Screener
# Syntax dictates the screener.snapshop takes the picture
#   and the 'Homepage' part is what the screenshot is called
driver.execute_script('/*@screener.snapshot*/', 'Google Homepage')

# Finding an element
interact = driver.find_element_by_name('q')

# Using the selected element
interact.send_keys('chupacabra')
interact.submit()
# interact.click()

driver.execute_script('/*@screener.snapshot*/', 'Chupacabra Results')

# Saving an extra screenshot
# driver.save_screenshot('screenshot.png')

# Using Action chains
# ActionChains(driver).move_to_element(interact).perform()

# Sauce Labs specific executors
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Notes here')

# Setting the job status to passed
driver.execute_script('sauce:job-result=passed')

# Ending the test session
driver.quit()

