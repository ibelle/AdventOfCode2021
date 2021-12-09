import os
import io
import re


# Read File 
with open('input.txt', mode='r+t') as f:
	increases = 0
	prev_depth = None
	for line in f.readlines():
		curr_depth = int(line)
		if prev_depth is not None and curr_depth > prev_depth:
			increases+=1
		prev_depth = curr_depth

	print(increases)
