import itertools as itools
import collections

# gamma_rate = []
# epsilon_rate = []
counts = collections.defaultdict(lambda: [0,0])
with open('input.txt', mode='r+t') as f:
	for line in f.readlines():
		line = line.strip()
		binary_as_list = [int(char) for char in line]
		# Count 1's and 0's by position
		for pos, bin_num in enumerate(binary_as_list):
			if bin_num:
				counts[pos][1]+=1 # increment Ones
			else:
				counts[pos][0]+=1 # increment Zeros

	epsilon_rate = ''
	gamma_rate = ''
	# Determine epsilon and gamma bit by position counts
	for pos, zero_count, ones_count in counts.items():
		print(pos, zero_count,ones_count)
		


