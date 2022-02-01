# SHA-256-Simplified-Implementation

A personal project in Python to implement and understand the working of the SHA-256 algorithm.
It comprises 3 main files that carry out the actual implementation - sha256.py, processor_funcs.py, helper_funcs.py
And 2 support files for cross-checking values as per the documentation (NIST-FIPS-180-4) - check_my_calcs.py, sha256_v2.py


In general, maximum data length is 2^64 bits. (2^64/8 bytes = 2^61 ASCII characters)
This code limits data input to 55 ASCII characters.
