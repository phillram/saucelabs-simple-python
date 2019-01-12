#This is not yet a complete script. I'm adding a W3C compatible version of the previous scripts. This will be what's used in the future for Selenium.



from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "Windows 10",
    'browserName': "chrome",
    'browserVersion': "69",
    'goog:chromeOptions':{"w3c": True},
    'sauce:options':{
        "name":"Chrome W3C Test", 
    }
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()