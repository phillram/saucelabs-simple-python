####################################################################
# Skeleton for Appium RDC tests on Test Object
####################################################################


###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import multiprocessing
import sys
from reusableFxns import *
androidTest = False
iosTest = False

###################################################################
# This makes the functions below execute "run" amount of times
###################################################################

run = 3

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################

#androidTest = True
#iosTest = True


###################################################################
# Declare as a function in order to do multiple runs
###################################################################

def run_sauce_test():
    ###################################################################
    # Common parameters (desired capabilities)
    # For Test Object tests
    ###################################################################
    projectParameters = {
        'testobject_api_key' : 'APIKEY', #The API generated for the Test Object project
        'appiumVersion': '1.8.1',
        'name': 'Run: ' + getNumber(),

    }
    
    androidParameters = { #Define Android parameters here
        'deviceName' : 'Google Pixel',
        'platformVersion' : '9',
        'browserName' : 'Chrome',
        'deviceOrientation' : 'portrait',
        'platformName' : 'Android',
    }
    
    iosParameters = { #Define iOS Parameters here
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
        print "You need to specify a platform to test on!"
        sys.exit()    
    elif androidTest == True and iosTest == True: 
        print "Don't be greedy! Only choose one platform!"
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
        #command_executor='https://eu1.appium.testobject.com/wd/hub',
        desired_capabilities=sauceParameters)
    
    ###################################################################
    # Test logic goes here
    ###################################################################
    
    #driver.get("https://phillip3369.wixsite.com/phill")
    
    interact = driver.find_element_by_id('comp-jkemo43ginput')
    interact.clear()
    interact.send_keys("poop")
    
    driver.save_screenshot('screenshot.png') 
    
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

