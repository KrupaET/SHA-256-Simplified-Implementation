'''
=====================SHA-256==================
In general maximum data length is 2^64 bits. (2^64/8 bytes = 2^61 ASCII characters)
This code limits data input 55 ASCII characters.
'''

import helper_funcs as hf
import processor_funcs as pf
import check_my_calcs as cmc

def main():
	# DATA INPUT AND HANDLING
	data = input("Enter data to hash (MAX 55 Symbols): ")
	if len(data) > 55:
		print("Data length exceeds 55 symbols!")
		exit(1)
	padded_data = hf.padData(data)
	print("\nPADDED DATA:-\n%s" %(padded_data))

	# INITIALISING ALL CONSTANTS
	primes_base = hf.findPrimes(64)
	printable_hv, hash_values = hf.findHashValues(primes_base)
	printable_rc, round_constants = hf.findRoundConstants(primes_base)
	#print("Cross-checking Hash Values... ? ", cmc.checkHashValues(printable_hv))
	#print("Cross-checking Round Constants... ? ", cmc.checkRoundConstants(printable_rc))
	print("\nINITIAL HASH VALUES:-\n", printable_hv)
	#print("\nACTUAL INITIAL HASH VALUES:-\n", hash_values)
	print("\nROUND CONSTANTS:-\n", printable_rc)
	#print("\nACTUAL ROUND CONSTANTS:-\n", round_constants)

	# SETTING UP PROCESSING FUNCTIONS AND MESSAGE SCHEDULE
	#print("Cross-checking Processing Functions... ?\n", cmc.checkProcessingFuncs())
	words = hf.initMessageSchedule(padded_data)
	printable_words, words = pf.findWords(words)
	print("\nMESSAGE SCHEDULE:-\n", printable_words)
	#print("\nACTUAL MESSAGE SCHEDULE:-\n", words)

	# HASH COMPRESSION
	hex_digest = pf.hashCompression(words, round_constants, hash_values)
	print("\nSHA-256 HASH:-\n", hex_digest, end = "\n\n")
	print("Cross-checking Hash Digest... ? ", cmc.checkSHA256(data, hex_digest))

if __name__ == "__main__":
	main()