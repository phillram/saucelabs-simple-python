####################################################################
# Skeleton for Selenium tests on Screener
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from time import sleep
import os
import urllib3

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Common parameters (desired capabilities)
###################################################################
screenerParameters = {
    # These Screener capablities are required. You'll find the apiKey and group name in the Screener.io dashboard
    'browserName': 'chrome',
    'screener': {
        'apiKey': os.environ['SCREENER_API_KEY'],
        'group': os.environ['SCREENER_GROUP_KEY'],
        'name': 'Visual Test',
        'resolution': '1920x1200',
    },

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
    #     'log': {'level': 'trace'},
    # },
}

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

# Using Action chains
# ActionChains(driver).move_to_element(interact).perform()

# Ending the test session
driver.quit()

