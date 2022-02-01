import processor_funcs as pf
import numpy as np
import hashlib

# Cross-checks generated constants and hash digest with predetermined ones.
def checkHashValues(my_hv):
	squares = "0x6a09e667 0xbb67ae85 0x3c6ef372 0xa54ff53a 0x510e527f 0x9b05688c 0x1f83d9ab 0x5be0cd19"
	correct = np.array(squares.split(" "))
	comp = correct == my_hv
	return comp.all()

def checkRoundConstants(my_rc):
	cubes = "0x428a2f98 0x71374491 0xb5c0fbcf 0xe9b5dba5 0x3956c25b 0x59f111f1 0x923f82a4 0xab1c5ed5 0xd807aa98 0x12835b01 0x243185be 0x550c7dc3 0x72be5d74 0x80deb1fe 0x9bdc06a7 0xc19bf174 0xe49b69c1 0xefbe4786 0x0fc19dc6 0x240ca1cc 0x2de92c6f 0x4a7484aa 0x5cb0a9dc 0x76f988da 0x983e5152 0xa831c66d 0xb00327c8 0xbf597fc7 0xc6e00bf3 0xd5a79147 0x06ca6351 0x14292967 0x27b70a85 0x2e1b2138 0x4d2c6dfc 0x53380d13 0x650a7354 0x766a0abb 0x81c2c92e 0x92722c85 0xa2bfe8a1 0xa81a664b 0xc24b8b70 0xc76c51a3 0xd192e819 0xd6990624 0xf40e3585 0x106aa070 0x19a4c116 0x1e376c08 0x2748774c 0x34b0bcb5 0x391c0cb3 0x4ed8aa4a 0x5b9cca4f 0x682e6ff3 0x748f82ee 0x78a5636f 0x84c87814 0x8cc70208 0x90befffa 0xa4506ceb 0xbef9a3f7 0xc67178f2"
	correct =  np.array(cubes.split(" "))
	comp = correct == my_rc
	return comp.all()

def checkSHA256(data, my_hd):
	theirs = (hashlib.sha256(data.encode())).hexdigest()
	print("Python: ", theirs)
	if my_hd == theirs:
		return True
	else:
		return False

# Predefined lambda functions (from the Documentation)
ROR = lambda x, y: (((x & 0xffffffff) >> (y & 31)) | (x << (32 - (y & 31)))) & 0xffffffff
Ch = lambda x, y, z: (z ^ (x & (y ^ z)))
Maj = lambda x, y, z: (((x | y) & z) | (x & y))
S = lambda x, n: ROR(x, n)
R = lambda x, n: (x & 0xffffffff) >> n
Sigma0 = lambda x: (S(x, 2) ^ S(x, 13) ^ S(x, 22))
Sigma1 = lambda x: (S(x, 6) ^ S(x, 11) ^ S(x, 25))
Gamma0 = lambda x: (S(x, 7) ^ S(x, 18) ^ R(x, 3))
Gamma1 = lambda x: (S(x, 17) ^ S(x, 19) ^ R(x, 10))

def checkProcessingFuncs():
	#print("DOCS\tMINE")
	print(R(5,2), pf.SHR(5,2))
	print(ROR(5,2), pf.ROR(5,2))
	print(Ch(15,6,2), pf.Ch(15,6,2))
	print(Maj(15,6,2), pf.Maj(15,6,2))
	print(Sigma0(12345), pf.Sigma0(12345))
	print(Sigma1(12345), pf.Sigma1(12345))
	print(Gamma0(12345), pf.Gamma0(12345))
	print(Gamma1(12345), pf.Gamma1(12345))
