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
