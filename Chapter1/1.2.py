def rev(string):
    i = 0
    j = len(string) - 1
    str_lst = list(string)
    while i < j:
        temp = str_lst[i]
        str_lst[i] = str_lst[j]
        str_lst[j] = temp
        i += 1
        j -= 1
    new_string = ""
    for char in str_lst:
        new_string += char
    print(new_string)

def main():
    cases = int(raw_input())
    for _ in range(cases):
        string = raw_input()
        print(string)
        rev(string)

if __name__ == "__main__":
    main()
