import numpy as np

# x, y, z, n are 32-bit words
# 2 parallel non-linear functions Ch and Maj for One-Way-Functionality
# Gamma0 and Gamma1 promote collision resistance
# 2 diffusion primitives Sigma1 and Sigma0 that increase scrambling
# Heavy feedback on working variables in the diffusion loop

WORDSIZE = 32
SHR = lambda x, n: x >> n
SHL = lambda x, n: x << n
ROR = lambda x, n: SHR(x & 0xffffffff, n & 31) | SHL(x, (WORDSIZE-(n & 31))) & 0xffffffff

Ch =  lambda x, y, z: (x & y) ^ (~x & z)
Maj = lambda x, y, z: (x & y) ^ (x & z) ^ (y & z)

Sigma0 = lambda x: (ROR(x, 2) ^ ROR(x, 13) ^ ROR(x, 22)) #uppersigma0
Sigma1 = lambda x: (ROR(x, 6) ^ ROR(x, 11) ^ ROR(x, 25)) #uppersigma1
Gamma0 = lambda x: (ROR(x, 7) ^ ROR(x, 18) ^ SHR(x, 3)) #lowersigma0
Gamma1 = lambda x: (ROR(x, 17) ^ ROR(x, 19) ^ SHR(x, 10)) #lowersigma1


# Determines the 17th to 64th words in the message schedule
def findWords(words):
	utility_list = []
	
	for t in range(16, len(words)):
		words[t] = (Gamma1(words[t-2]) + words[t-7] + Gamma0(words[t-15]) + words[t-16]) % (2**32)
	
	for i in range(len(words)):
		utility_list.append("{:032b}".format(words[i]))
	
	utility_list = np.array(utility_list)
	words = np.array(words)
	return utility_list, words


# Creates the message digest using Sigma0, Sigma1, Ch and Maj
def hashCompression(words, round_constants, hash_values):
	# make sure addition is modulo 2^32
	digest_64, digest_256, temp1, temp2 = "", "", 0, 0
	# Working variable set
	a = hash_values[0]
	b = hash_values[1]
	c = hash_values[2]
	d = hash_values[3]
	e = hash_values[4]
	f = hash_values[5]
	g = hash_values[6]
	h = hash_values[7]

	for t in range(len(words)):
		temp1 = (h + Sigma1(e) + Ch(e ,f, g) + round_constants[t] + words[t]) % 2**32
		temp2 = (Sigma0(a) + Maj(a, b, c)) % 2**32
		h = g
		g = f
		f = e
		e = (d + temp1) % 2**32
		d = c
		c = b
		b = a
		a = (temp1 + temp2) % 2**32
	
	hash_values[0] = (a + hash_values[0]) % 2**32
	hash_values[1] = (b + hash_values[1]) % 2**32
	hash_values[2] = (c + hash_values[2]) % 2**32
	hash_values[3] = (d + hash_values[3]) % 2**32
	hash_values[4] = (e + hash_values[4]) % 2**32
	hash_values[5] = (f + hash_values[5]) % 2**32
	hash_values[6] = (g + hash_values[6]) % 2**32
	hash_values[7] = (h + hash_values[7]) % 2**32
	#print("\nMODIFIED HASH VALUES:-\n", hash_values)
	
	for i in hash_values:
		digest_256 += bin(i)[2:].rjust(32, '0')
		digest_64 += hex(i)[2:].rjust(8, '0')
	#print("\n-------------256-Bit Digest------------\n%s\nLength = %d" %(digest_256, len(digest_256)))
	return digest_64
