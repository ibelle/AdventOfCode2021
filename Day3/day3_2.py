import collections

digit_counts = collections.defaultdict(lambda: [0,0])
all_numbers = []
with open('input.txt', mode='r+t') as f:
	for line in f.readlines():
		line = line.strip()
		binary_as_list = [int(char) for char in line]
		all_numbers.append(binary_as_list)
        # Count 1's and 0's by position
		for pos, bin_num in enumerate(binary_as_list):
			if bin_num:
				digit_counts[pos][1]+=1 # increment Ones
			else:
				digit_counts[pos][0]+=1 # increment Zeros
print(digit_counts)

o2_gen_values = []
co2_scrubber_values = []
for number in all_numbers:
    for pos, digit in enumerate(number):
        zero_cnt, ones_cnt = digit_counts[pos]
        mc_bit = 0 if zero_cnt > ones_cnt else 1
        bit_eq = zero_cnt == ones_cnt
        if digit == mc_bit:
            
        else:



        

        # if (zero_cnt >= ones_cnt) and digit == 

