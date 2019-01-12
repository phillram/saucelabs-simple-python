####################################################################
# Minimal script to connect to Sauce Labs RDC
# All this does is connect to your project and start a test
# wait 30 seconds. Then quit test
####################################################################


from appium import webdriver
from time import sleep

sauceParameters = {
    'appiumVersion': '1.8.1',
    'deviceName' : 'Google Pixel 2',
    'deviceOrientation' : 'portrait',
    'browserName' : 'Chrome',
    'platformVersion' : '9',
    'platformName' : 'Android',
    'testobject_api_key' : 'APIKEY', # Plug in your project API key here
}



driver = webdriver.Remote(
    command_executor='https://us1.appium.testobject.com/wd/hub',
    desired_capabilities=sauceParameters)


sleep(30)

driver.quit()