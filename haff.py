
def count_symbols(s, myset):
	frequency = []
	for one_symbol in myset:
		frequency.append([one_symbol, s.count(one_symbol)])
	frequency.sort(key = lambda val: val[1])
	return frequency

def binarator(curr, index):
	if(isinstance(curr, list)):
		print(index)
		binarator(curr[0], index + '0')
		binarator(curr[1], index + '1')
	elif(isinstance(curr, str)):
		print([curr, index])
		return [curr, index]
	elif(isinstance(curr, int)):
		return curr

s = list('beep boop beer!')

myset = set(s)
frequency = count_symbols(s, myset)
decoder = frequency 

# print (frequency)

while len(frequency) > 1:
	(first, second) = frequency[:2]
	new_elem = [[[first[0], second[0]], first[1] + second[1]]]
	frequency = new_elem + frequency[2:]
	frequency.sort(key = lambda val: val[1])

#nex row is making me mad!
frequency = frequency[0][0]

print (frequency)

print(binarator(frequency, ''))
