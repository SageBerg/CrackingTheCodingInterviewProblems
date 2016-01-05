def permutations(string, lst):
    if len(string) != 1:
        permutations(string[1:], lst)
    else:
        lst.append(string[0])
        return
    new_lst = []
    for item in lst:
        for i in range(len(item)):
            new_lst.append(item[:i] + string[0] + item[i:])
        new_lst.append(item + string[0])
    lst += new_lst

def remove_small_values(string, lst):
    new_list = []
    for value in lst:
        if len(value) == len(string):
            new_list.append(value)
    return new_list

def main():
    lst = []
    test = "abcd"
    permutations(test, lst)
    lst = remove_small_values(test, lst)
    print lst, len(lst)

main()
