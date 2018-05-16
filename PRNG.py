import math
import time
import random
import hashlib
import random
import numpy


#====================================================================
# Using the in-built Random Function
# The Mersenne Twister is a pseudorandom number generator (PRNG). 
# It is by far the most widely used general-purpose PRNG.
# It was the first PRNG to provide fast generation of high-quality pseudorandom integers.

seed1 = ('Sys', 'Sec')
str1  = u''.join(seed1).encode('utf-8')
# On python 3.3+ running hash against your tuple gives you a unique value each time.
sha   = hashlib.sha1(str1)			# Perform Hash Operation
random.seed(sha.hexdigest())		# Use the digest obtained as the seed
a = random.getrandbits(32217)
#a = 4
seq1 = bin(a)[2:]
							# Select seq1
#print seq1

#====================================================================

# Linear Congruential Random Number Generator

# A linear congruential generator (LCG) is an algorithm 
# that yields a sequence of pseudo-randomized numbers 
# calculated with a discontinuous piecewise linear equation. 

# r_{n+1} = a * r_{n} + c (mod m)

# 	r_{0}	    is the seed
# 	r_{n}		are random numbers
# 	a, c, m 	are constants
# The randomness is dependent on the values of a, c and m too.
# The implementation must yield the same sequence of integers for the same seed

 #Choosing seeds according to the BSD Formula
 # a = 1103515245
 # b = 12345
 # c = 2^31


def lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) & 0x7fffffff
	yield seed

seq=0
seed = random.randint(0, 0x7fffffff)

snippet = lcg(seed)
for i in range (1024):
	seq = str(seq) + str(snippet.next()) 


seq  = int (seq)
seq2 = bin(seq)[2:]
								#Select Seq 2
print seq2

#====================================================================
#====================================================================
