def largest_sum(array):
    max_sum = array[0]
    cur_sum = array[0]
    i = 1
    while i < len(array):
       	if cur_sum > 0 and cur_sum + array[i] > 0:
            cur_sum = cur_sum + array[i]
        else:
            cur_sum = array[i]
        if cur_sum > max_sum:
            max_sum = cur_sum        
        i += 1
    return max_sum

def condense(array):
    new_array = []
    current_number = array[0]
    for i in range(1, len(array)):
        if (current_number < 0 and array[i] < 0) or \
           (current_number >= 0 and array[i] >= 0):
            current_number += array[i]
        else:
            new_array.append(current_number)
            current_number = array[i]
    new_array.append(current_number)
    return new_array

print largest_sum(condense([ 2, 3, -8, -1, 2, 4, -2, 3]))
print largest_sum(condense([ 11, 0, -1, -5, -4, 8, 4, -2, 3, -1]))
