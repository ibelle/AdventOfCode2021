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
	for pos, binary_counts in counts.items():
		zero_cnt, ones_cnt = binary_counts
		if zero_cnt > ones_cnt:
			epsilon_rate += '1'
			gamma_rate += '0'
		else:
			epsilon_rate += '0'
			gamma_rate += '1'			
	print(int(epsilon_rate, 2) * int(gamma_rate, 2))