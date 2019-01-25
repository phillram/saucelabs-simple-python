####################################################################
# Skeleton for Appium tests on Sauce Labs RDC
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import multiprocessing
import sys
from reusableFxns import *
import requests
androidTest = False
iosTest = False

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################

run = 2

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

# androidTest = True
# iosTest = True


###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Test Object tests
    ###################################################################
    projectParameters = {
        'testobject_api_key' : 'APIKEY', # The API generated for the Test Object project
        'appiumVersion': '1.8.1',
        'name': 'Run: ' + getNumber(),
        # 'nativeWebTap': True,
    }
    
    androidParameters = { # Define Android parameters here
        'deviceName' : 'Google Pixel',
        'platformVersion' : '9',
        'browserName' : 'Chrome',
        'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
    }
    
    iosParameters = { # Define iOS Parameters here
        'deviceName' : 'iPhone X',
        'deviceOrientation' : 'portrait',
        'browserName' : 'safari',
        'platformVersion' : '11.4.1',
        'platformName' : 'iOS',
        
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

    # Updating the test to pass/fail via the API
    #__________________________________________________________________
    requests.put(
        'https://app.testobject.com/api/rest/v2/appium/session/' + driver.session_id + '/test/',
        headers = { 'Content-Type': 'application/json',},  
        data = '{"passed": true}' # Update this to pass either True or False depending on your requirements
    )

    # Ending the test session
    #__________________________________________________________________
    driver.quit()






###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################

if __name__ == '__main__':
    jobs = [] #Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) #Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() #Start the functions.
        # print('this is the run for: '+ str(i))

