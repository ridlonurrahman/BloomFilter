#!/usr/bin/python
'''
TASK 7 BLOOMFILTER

'''


import sys
import math
from bitarray import bitarray

# init n, p, m, k, and bloomfilter array
n = int(sys.argv[1])
p = 0.01
m = int(math.ceil((n * math.log(p)) / math.log(1.0 / (pow(2.0, math.log(2.0))))))
k = int(round(math.log(2.0) * m / n))
bit_array = [0]*m

for line in sys.stdin:
	line = line.strip()
	#hashing line
	index_hashed = [hash(line+'exc'*j)%m for j in range(k)]
	
	#if there is line isn't in filter, update filter, and print line
	if [bit_array[idx] for idx in index_hashed]!=[1]*k:
		for idx in index_hashed:
			bit_array[idx]=1
		print(line)
