import sys, json

myfile = open(sys.argv[1], 'r')
frequency = (json.load(myfile))
myfile.close()
code = frequency[-1]
frequency = frequency[:-1]
print (code)

for word in code.split():
	element = frequency
	for symbol in word:
		element = element[int(symbol)]
	print (element)
