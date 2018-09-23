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

countFilePath = Path('saucelabs-simple-python\countFile.txt')

def getNumber(filename = countFilePath):
    with open(filename, "r+") as f:
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        f.close()
        print ('This is test run: ' + str(val))
        return str(val)
