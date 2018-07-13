# simple script to split a csv of 3D located annotations into seperate files for use within Cloud Compare
# requires a file of format ID, X, Y, Z, description, anything else
# anything after Z will be ignored.
# outputs files to parent directory of source file

# no copyright and no liability.

# accept argument of file to process.

import sys
import os.path
filevar = sys.argv[1]  							# get file to parse from terminal

def processLine (line) :
    line_ar = line.split(',')
    # make sure that the row being processed has at least 4 (id x y z) components, otherwise it's not valid
    if len(line_ar) > 4 :
        d = os.path.dirname(filevar) + "/"
        filename = d + line_ar[0] + ".csv"
        # make new content out of the xyz of the row
        content = line_ar[1] + ',' + line_ar[2] + ',' + line_ar[3]
        nf = open (filename, 'w')
        nf.write(content)
        nf.close
        return(filename + ' : ' + content)

f = open(filevar,'r')                           # read input file
for line in f:
    processLine (line)

print ("files saved in" + os.path.abspath(filevar))
