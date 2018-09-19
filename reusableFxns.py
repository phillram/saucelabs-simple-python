####################################################################
# Functions to be reused across other files
####################################################################


###################################################################
# This opens a file to increment the number
###################################################################
def getNumber(filename="countFile.txt"):
    with open(filename, "r+") as f:
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        f.close()
        print ('This is test Run: ' + str(val))
        return str(val)
