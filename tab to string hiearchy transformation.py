# python script processing tabbed hierarchy into lightroom ">" notation
# original code by S. Pantos

def processLine(line, stack):
	splitline = line.split("\t")
	newline = ""
	if len(splitline) <= len(stack): # If the indentation has decreased we have reached the end and we need to print it out.
		i = 0
		for s in stack:
			if i < 1:
				newline += s
			else:
				newline +=  " > " + s
                	newstack = stack[0:len(splitline)-1] # Shorten the stack of values to remove the ones no longer needed
			i = i + 1
        else:
			newstack = stack
	newstack.append(splitline[-1])     # add the current value on to the stack of values.

	id = splitline[len(splitline)-1]

	print str(newline)
        return newstack

stack = []

f = open('/Users/hairyfreak/Desktop/keywords.txt', 'r')
for line in f:
    stack = processLine(line, stack)
processLine("", stack)
