current, counter, lst_counter = int(input()), 1, []
while current != 0:
    next = int(input())
    if next != 0 and next == current:
        counter += 1
    else:
        counter = 1
    current = next
    lst_counter.append(counter)
print(max(lst_counter))

'''
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
'''


