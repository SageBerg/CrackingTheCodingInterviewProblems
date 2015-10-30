def is_perm(string_1, string_2):
    strings = [string_1, string_2]
    char_maps = [dict(), dict()]
    for i in range(len(strings)):
        for char in strings[i]:
            if char not in char_maps[i]:
                char_maps[i][char] = 1
            else:
                char_maps[i][char] += 1
    for char in char_maps[0]:
	    if char in char_maps[0] and char not in char_maps[1] or \
           char_maps[0][char] != char_maps[1][char]:
                return False
    return True

def main():
    cases = int(raw_input())
    for _ in range(cases):
        two_strings = raw_input().split()
        string_1 = two_strings[0]
        string_2 = two_strings[1]
        print(string_1, string_2, is_perm(string_1, string_2))

if __name__ == "__main__":
    main()
