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
# from ./ import reusableFxns

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
# For Sauce Labs Tests
###################################################################
screenerParameters = {
    # These Screener capablities are required. You'll find the apiKey and group name in the Screener.io dashboard
    # Using the proxy flag will have the tests run on Sauce Labs cloud with your Sauce Labs credentials
    # This proxy will likely no longer be necessary when Screener is integrated into Sauce
    'screener': {
        'apiKey': os.environ['SCREENER_API_KEY'],
        'group': os.environ['SCREENER_GROUP_KEY'],
        'name': 'Visual Test',
        'resolution': '1280x1024',
        'proxy': 'https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com/wd/hub',
        # 'proxy': 'https://' + os.environ['SAUCE_USERNAME'] + ':' + os.environ['SAUCE_ACCESS_KEY'] + '@ondemand.eu-central-1.saucelabs.com',
    },
    # These are the capabilities that Selenium / Sauce Labs will use
    'tags':['Screener','Tests',],
    'platform': 'Windows 10',
    'browserName': 'firefox',
    'version': 'latest',
    # 'screenResolution':'1400x1050',
    'name': 'Run: ' + getNumber(),
    # 'tunnelIdentifier':'Phill Tunnel One',
    'seleniumVersion': '3.141.0',
    # 'iedriverVersion': '3.4.0',
    # 'chromedriverVersion': '2.40',
    # 'requireWindowFocus' : True,
    # 'maxDuration': 1800,
    # 'idleTimeout': 1000,
    # 'commandTimeout': 600,
    # 'videoUploadOnPass':False,
    # 'extendedDebugging':'true',
    # 'prerun':{ 
    #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
    #     'args': ['--silent'],
    #     'timeout': 500,
    #     'background': 'false',
    # },
    # 'chromeOptions':{
    #     mobileEmulation':{'deviceName':'iPhone X'},
    #     'prefs': {
    #         'profile': {
    #             'password_manager_enabled': False
    #             },
    #             'credentials_enable_service': False,
    #         },
    #     'args': ['test-type', 'disable-infobars'],
    # },
    # 'moz:firefoxOptions':{
    #     'log': {'level': 'trace'},
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
#__________________________________________________________________
driver.get('https://www.dryzz.com')

# Taking a screenshot on Screener
# Syntax dictates the screener.snapshop takes the picture
#   and the 'Homepage' part is what the screenshot is called
#__________________________________________________________________
driver.execute_script('/*@screener.snapshot*/', 'Homepage')

# Setup for finding an element and clicking it
#__________________________________________________________________
interact = driver.find_element_by_id('menu-item-112')
interact.click()
driver.execute_script('/*@screener.snapshot*/', 'Projects')

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
# driver.execute_script('sauce: job-result=passed')

# Ending the test session
#__________________________________________________________________
driver.quit()

