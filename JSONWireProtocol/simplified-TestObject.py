####################################################################
# Minimal script to connect to Sauce Labs RDC
# All this does is connect to your project and start a test
# wait 30 seconds. Then quit test
####################################################################

from appium import webdriver
from time import sleep

sauceParameters = {
    'testobject_api_key' : 'APIKEY', # Plug in your project API key here
    'deviceName' : '.*Pixel.*', 
    'platformName' : 'Android',
    'browserName' : 'Chrome',
    # The following are not required
    # 'deviceOrientation' : 'portrait',
    # 'platformVersion' : '10',
    # 'appiumVersion': '1.16.0',
}

driver = webdriver.Remote(
    command_executor='https://us1.appium.testobject.com/wd/hub',
    desired_capabilities=sauceParameters)

sleep(30)

driver.quit()