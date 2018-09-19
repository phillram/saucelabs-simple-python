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
from reusableFxns import *
iosTest = False
useApp = False

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

#androidTest = True
#iosTest = True

###################################################################
# Uncomment if this is an app test
# Add in the location to the stored app too
###################################################################

#useApp = True
appLocation = 'sauce-storage:app.apk'

###################################################################
# Common parameters (desired capabilities)
# For Test Object tests
###################################################################
projectParameters = {
    'tags':['Case', '1111',],
    'appiumVersion': '1.8.1',
    'name': 'Run: ' + getNumber(),
    #'autoAcceptAlerts':'true',
    #'locationServicesEnabled':'true',
    #'locationServicesAuthorized':'true',
}

androidParameters = { #Define Android parameters here
    'deviceName' : 'Google Pixel GoogleAPI Emulator',
    'platformVersion' : '7.1',
    'platformName' : 'Android',
    'deviceOrientation' : 'portrait',

}

iosParameters = { #Define iOS Parameters here
    'deviceName' : 'iPhone X Simulator',
    'deviceOrientation' : 'portrait',
    'platformVersion' : '11.3',
    'platformName' : 'iOS',
    
}

###################################################################
# Merge parameters into a single capability dictionary
###################################################################

sauceParameters = {}
sauceParameters.update(projectParameters)
sauceParameters.update({'build': '-'.join(projectParameters.get('tags'))}) # This concatenates the tags key above to add the build parameter


if androidTest != True and iosTest != True: 
    print("You need to specify a platform to test on!")
    sys.exit()    
elif androidTest == True and iosTest == True: 
    print("Don't be greedy! Only choose one platform!")
    sys.exit()    
elif androidTest:
    sauceParameters.update(androidParameters)
    if useApp:
        sauceParameters['app'] = appLocation #Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' #otherwise use browser
elif iosTest:
    sauceParameters.update(iosParameters)
    if useApp:
        sauceParameters['app'] = appLocation
    else:
        sauceParameters['browserName'] = 'safari'

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

interact = driver.find_element_by_id('site-navigation')
interact.click()

interact = driver.find_element_by_id('menu-item-112')
interact.click()

#driver.save_screenshot('screenshot.png')
#interact.send_keys("Dryzz")
#interact.submit()
#driver.execute_script('sauce: break')
#driver.execute_script("sauce:context=Place words here for notes")
driver.quit()





