####################################################################
# Functions to be reused across other files
####################################################################

###################################################################
# Imports that are good to use
# Predominately to find pathing between Windows and Unix
###################################################################
from pathlib import Path

###################################################################
# This opens a file to increment the number
###################################################################

countFilePath = Path('countFile.txt')

def getNumber(filename = countFilePath):
        with open(countFilePath, "r+") as countingFile:
                val = int(countingFile.read() or 0) + 1
                countingFile.seek(0)
                countingFile.truncate()
                countingFile.write(str(val))
                countingFile.close()
                # print ('This is test run: ' + str(val))
                return str(val)


###################################################################
# This is a list of the data center URLs.
# Mainly for reference, but you're welcome to use the variables
###################################################################

us_west_dc = 'ondemand.saucelabs.com/wd/hub'
us_east_dc = 'ondemand.eu-central-1.saucelabs.com/wd/hub'
eu_west_dc = 'ondemand.us-east-1.saucelabs.com/wd/hub'