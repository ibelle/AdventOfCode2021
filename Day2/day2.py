

HORIZONTAL_POS = 0
VERTICAL_POS = 0

def move_ship(dir, value):
	global HORIZONTAL_POS, VERTICAL_POS
	if dir == 'forward':
		HORIZONTAL_POS += value

	if dir == 'up':
		VERTICAL_POS = 0 if (VERTICAL_POS - value) < 0 else (VERTICAL_POS - value)

	if dir == 'down':
		VERTICAL_POS += value


with open('input.txt', mode='r+t') as f:
	for line in f.readlines():
		curr_dir, current_dist = line.split(' ')
		current_dist = int(current_dist)
		move_ship(curr_dir, current_dist)

status = ('HORIZONTAL_POS {}. VERTICAL_POS {}, '
		  'CALC_POS {}'.format(HORIZONTAL_POS, VERTICAL_POS, 
		  VERTICAL_POS * HORIZONTAL_POS))
print (status)