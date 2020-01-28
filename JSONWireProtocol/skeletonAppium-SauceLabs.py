####################################################################
# Skeleton for Appium Virtual Tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import sys
import os
androidTest = False
# from reusableFxns import *
iosTest = False
useApp = False

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

androidTest = True
# iosTest = True

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

region = 'US'

###################################################################
# Uncomment if this is an app test
# Add in the location to the stored app too
###################################################################

# useApp = True
appLocation = 'sauce-storage:app.apk'

###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################
projectParameters = {
    'tags':['Case', '1111',],
    'appiumVersion': '1.8.1',
    # 'name': 'Run: ' + getNumber(),
    # 'autoAcceptAlerts':'true',
    # 'locationServicesEnabled':'true',
    # 'locationServicesAuthorized':'true',
    'extendedDebugging': 'true',
    'capturePerformance': 'true'
}

androidParameters = { # Define Android parameters here
    'deviceName' : 'Google Pixel GoogleAPI Emulator',
    'platformVersion' : '7.1',
    'platformName' : 'Android',
    'deviceOrientation' : 'portrait',

}

iosParameters = { # Define iOS Parameters here
    'deviceName' : 'iPhone X Simulator',
    'deviceOrientation' : 'portrait',
    'platformVersion' : '11.3',
    'platformName' : 'iOS',
    # 'nativeWebTap': True, # iOS only capability.
}

###################################################################
# Merge parameters into a single capability dictionary
###################################################################

sauceParameters = {}
sauceParameters.update(projectParameters)
sauceParameters.update({'build': '-'.join(projectParameters.get('tags'))}) # This concatenates the tags key above to add the build parameter


if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)
    if useApp:
        sauceParameters['app'] = appLocation # Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
        #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
elif iosTest:
    sauceParameters.update(iosParameters)
    if useApp:
        sauceParameters['app'] = appLocation
    else:
        sauceParameters['browserName'] = 'safari'

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
