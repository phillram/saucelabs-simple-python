####################################################################
# Skeleton for Appium tests on Sauce Labs RDC
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import multiprocessing
import urllib3
import requests
import json
import random
import sys

androidTest = False
iosTest = False

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Pull a random Pokemon name to use as the test name
###################################################################
pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
random_pokemon = random.choice(pokemon_names)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
# iosTest = True

###################################################################
# Common parameters (desired capabilities)
###################################################################
projectParameters = {
    'testobject_api_key' : 'APIKEY', # The API generated for the Test Object project
    # The following are not required
    'name': random_pokemon,
    # 'deviceOrientation' : 'portrait',
    # 'appiumVersion': '1.16.0',
}

androidParameters = { # Define Android parameters here
    'deviceName' : '.*Pixel.*',
    'platformName' : 'Android',
    'browserName' : 'Chrome',
    'platformVersion' : '10',
}

iosParameters = { # Define iOS Parameters here
    'deviceName' : 'iPhone.*',
    'platformVersion' : '13',
    'platformName' : 'iOS',
    'browserName' : 'safari',
    # 'nativeWebTap': 'true',
}

###################################################################
# Merge parameters into a single capability dictionary
###################################################################
sauceParameters = {}
sauceParameters.update(projectParameters)
if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)
elif iosTest:
    sauceParameters.update(iosParameters)

###################################################################
# Connect to Test Object (RDC Cloud)
###################################################################
driver = webdriver.Remote(
    command_executor='https://us1.appium.testobject.com/wd/hub',
    # command_executor='https://eu1.appium.testobject.com/wd/hub',
    desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
driver.get('https://www.google.com')

# Finding an element
interact = driver.find_element_by_name('q')

# Using the selected element
interact.send_keys('chupacabra')
interact.submit()
# interact.click()

# Saving an extra screenshot
driver.save_screenshot('screenshot.png')

# Using Action chains
# ActionChains(driver).move_to_element(interact).perform()

# Sauce Labs specific executors
# driver.execute_script('sauce: break')
# driver.execute_script('sauce:context=Notes here')

# Updating the test to pass/fail via the API
requests.put(
    'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
    headers = { 'Content-Type': 'application/json',},
    data = '{"passed": true}' # Update this to pass either True or False depending on your requirements
)

# Ending the test session
driver.quit()
