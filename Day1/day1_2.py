WINDOW_SIZE = 3

with open('input.txt', mode='r+t') as f:
    increases = 0
    prev_depth = None
    current_window = []
    prev_window = []
    for line in f.readlines():
        curr_depth = int(line)
        current_window.append(curr_depth)
        if len(current_window) == WINDOW_SIZE:
            curr_window_depth = sum(current_window)
            if prev_window:
                prev_window_depth = sum(prev_window)
                if curr_window_depth > prev_window_depth:
                    increases+=1
            prev_window = current_window[:] #prev_window = current_window
            current_window = current_window[1:] #Current window slides window down by 1

    print(increases)
