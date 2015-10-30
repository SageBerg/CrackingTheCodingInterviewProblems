def all_unique(string):
    chars = {}
    for char in string:
        if char in chars:
            return False
        else:
            chars[char] = 1
    return True

def all_unique_no_data_structures(string):
    for char in string:
        if not char_check(string, char):
            return False
    return True

def char_check(string, char):
    char_count = 0
    for char in string:
        if char == char:
            char_count += 1
            if char_count > 1:
                return False
    return True


def main():
    cases = int(raw_input())
    for _ in range(cases):
        string = raw_input()         
        print(string, all_unique(string))
        print(string, all_unique_no_data_structures(string))

if __name__ == "__main__":
    main()
