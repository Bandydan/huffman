import json
import sys

def count_symbols(s, myset):
	frequency = []
	for one_symbol in myset:
		frequency.append([one_symbol, s.count(one_symbol)])
	frequency.sort(key = lambda val: val[1])
	return frequency

def binarator(curr, index):
	if(isinstance(curr, list)):
		# print(index)
		binarator(curr[0], index + '0')
		binarator(curr[1], index + '1')
	elif(isinstance(curr, str)):
		# print([curr, index])
		mydict[curr] = index
		return
	elif(isinstance(curr, int)):
		return

# s = list('beep boop beer!')
s = list('There should be more in life then this! I can not believe that is the end')

myset = set(s)
mydict = {}
frequency = count_symbols(s, myset)
print(frequency)

# decoder = frequency

# print (frequency)

while len(frequency) > 1:
	(first, second) = frequency[:2]
	new_elem = [[[first[0], second[0]], first[1] + second[1]]]
	frequency = new_elem + frequency[2:]
	# print(frequency)
	frequency.sort(key = lambda val: val[1])

#next row is making me mad!
frequency = frequency[0][0]

# print (frequency)

binarator(frequency, '')
print (mydict)

coded_string = ''
for one_symbol in s:
	coded_string += mydict[one_symbol]

print(coded_string)
frequency.append(coded_string)

print(json.dumps(mydict))
myfile = open(sys.argv[1], 'w')
myfile.write(json.dumps(frequency))
myfile.close()

# l = [int(s[i:i+k],base=2) for i in range(0, len(s), 8)]

# ll = [bin(i) for i in l]

