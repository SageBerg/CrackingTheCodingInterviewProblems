def has_magic_index(lst): #for sorted list with distinct values
    for i in range(len(lst)):
        if lst[i] > i:
           return False
        if lst[i] == i:
           return i
    return False

def has_magic_index_non_distict(lst):
    for i in range(len(lst)):
        if lst[i] == i:
            return i
    return False

def smarter_has_magic_index(lst, index_offset):
    middle = len(lst) / 2
    if lst[middle] == middle + index_offset:
        return middle + index_offset
    elif lst[middle] < middle + index_offset and len(lst) > 1:
        return smarter_has_magic_index(lst[middle:], index_offset + middle)
    else:
        if len(lst) > 1:
            return smarter_has_magic_index(lst[:middle], index_offset)
    return False

def main():
    #print has_magic_index([-10, 2, 3, 4])
    #print has_magic_index([-10, 0, 2, 4])
    #print has_magic_index_non_distict([-10, 2, 3, 4])
    #print has_magic_index_non_distict([-10, 0, 3, 3])
    print smarter_has_magic_index([-10, 2, 3, 4], 0)
    print smarter_has_magic_index([0] + range(2, 20), 0)
    print smarter_has_magic_index(range(-1, 100) + [101], 0)

main()
