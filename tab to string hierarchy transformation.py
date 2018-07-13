# python script processing tabbed hierarchy into lightroom ">" notation
# Can be used in conjunction with open refine or a database structure to allow clean import
# of hiearchical keywords into Adobe Lightroom catalogue using LR transporter plugin.
# based on original code by S. Pantos 2018

# use from terminal from folder prompt:python this_script.py file_to_convert.txt
# outputs to terminal
# edit output with texteditor of your choice (e.g. Atom) and then open refine thus:

# that needs cleaning in atom first.
# change \n > to  >
# change \n\n to \n

# load lines into open refine then use these saved actions:
# openrefine-convert lightroom keywords lists.texteditor
# or do this
# explode out {} into synonyms column (make su reyou keep the column)
# 	delete the first column
# 	then (blank down on the first column)
# 	cells -> merge multivalue cells
#	slice, pop off, extract last word from a hiearchy string with:
# 		if (lastIndexOf(value," > ") > 0, slice(value,lastIndexOf(value," > ")+3),value)
#	move to first column


# No liability, no copyright. Made for specific use case.
import sys
filevar = sys.argv[1]  							# get file to parse from terminal

def processLine(line, stack):
	splitline = line.split("\t")
	newline = ""
#	print(len(splitline))
#	print(len(stack))
	if len(splitline) <= len(stack): 			# If the indentation has decreased or stayed the same we have reached the end and we need to traverse back.
		newstack = stack[0:len(splitline)-1]	# Shorten the stack of values to remove the ones no longer needed
	else:
		newstack = stack
	newstack.append(splitline[-1])			# add the current value on to the stack of values.

	# loop through the current stack and generate output
	i = 0 									# just a pointer
	for s in newstack:
		if i < 1:
			newline += s 					# add parent category without prefix
		else:
			newline +=  " > " + s			# add > prefix to sub categories
		i = i + 1							# move pointer

	print str(newline)						# print hierarchy of current line
	return newstack							# output the the clipped stack to be traversed

stack = []									# initialize
f = open(filevar, 'r')						# open file
for line in f:
    stack = processLine(line, stack)
