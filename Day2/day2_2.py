

HORIZONTAL_POS = 0
VERTICAL_POS = 0
_AIM = 0

def move_ship(dir, value):
	global HORIZONTAL_POS, VERTICAL_POS, _AIM
	if dir == 'forward':
		HORIZONTAL_POS += value
		VERTICAL_POS += value * _AIM # if aim==0?

	if dir == 'up':
		#VERTICAL_POS = 0 if (VERTICAL_POS - value) < 0 else (VERTICAL_POS - value)
		_AIM = 0 if (_AIM - value) < 0 else (_AIM - value)

	if dir == 'down':
		_AIM += value


with open('input.txt', mode='r+t') as f:
	for line in f.readlines():
		curr_dir, current_dist = line.split(' ')
		current_dist = int(current_dist)
		move_ship(curr_dir, current_dist)

status = ('HORIZONTAL_POS {}. VERTICAL_POS {}, '
		  'CALC_POS {}'.format(HORIZONTAL_POS, VERTICAL_POS, 
		  VERTICAL_POS * HORIZONTAL_POS))
print (status)