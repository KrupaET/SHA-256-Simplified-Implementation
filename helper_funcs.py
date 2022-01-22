import numpy as np
import math

# Pads input data in binary as per MD Strengthening process
def padData(data):
	bin_data = ''.join(format(ord(i), '08b') for i in data)
	#print("Binary representation: ", bin_data)

	bin_length = bin(len(bin_data))[2:]
	#print("Length of binary data in binary: ", bin_length)
	
	bin_data += '1'

	padded_data = bin_data.ljust(448, '0') + bin_length.rjust(64, '0')
	#print("Padding 448 bits: ", bin_data.ljust(448, '0'))
	#print("Padding last 64 bits: ", bin_length.rjust(64, '0'))
	return padded_data


# Finds first n prime numbers
def findPrimes(n):
	trace, utility_list = 0, []
	flag, i = 0, 1
	
	while trace < n:
		i+=1
		flag = 0
		for j in utility_list:
			if i%j == 0:
				flag = 1
				break
		if flag == 0:
			utility_list.append(i)
			trace+=1
	
	primes_base = np.array(utility_list)
	#print("\nPRIMES GENERATED:-\n", primes_base)
	return primes_base


# Finds Hash Values as first 32 bits of square roots of first 8 primes
def findHashValues(primes_base):
	hash_values, utility_list = [], []
	sqrt_primes = np.sqrt(primes_base[:8])
	#print(sqrt_primes)

	for i in sqrt_primes:
		hash_values.append(int((math.modf(i))[0]*(1<<32)))
	
	for i in range(len(hash_values)):
		utility_list.append("0x{:08x}".format(hash_values[i]))
	
	hash_values = np.array(hash_values)
	utility_list = np.array(utility_list)
	return utility_list, hash_values


# Finds Round Constants as first 32 bits of cube roots of first 64 primes
def findRoundConstants(primes_base):
	round_constants, utility_list = [], []
	cbrt_primes = np.cbrt(primes_base)
	#print(cbrt_primes)	

	for i in cbrt_primes:
		round_constants.append(int((math.modf(i))[0]*(1<<32)))
	
	for i in range(len(round_constants)):
		utility_list.append("0x{:08x}".format(round_constants[i]))
	
	round_constants = np.array(round_constants)
	utility_list = np.array(utility_list)
	return utility_list, round_constants


# Initializes message schedule where first 16 words are padded data and next 48 words initialized to 0
def initMessageSchedule(padded_data):
	trace, utility_list, words = 0, [], []

	while trace<len(padded_data):
		utility_list.append(padded_data[trace:(trace+32)])
		trace+=32
	
	utility_list += ['0'*32]*48

	for i in range(len(utility_list)):
		words.append(int(utility_list[i], 2))
	
	words = np.array(words, dtype=np.int64)
	#print("Number of words in message schedule: ", len(words))
	return words
