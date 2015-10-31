def compress(string):
    compressed_string = ""
    i = 0
    while i < len(string):
        j = i
        letter_count = 0
        while string[j] == string[i]:
            letter_count += 1
            j += 1
            if j == len(string):
                break;
        compressed_string += string[i] + str(letter_count)
        i += letter_count
    if len(compressed_string) < len(string):
        return compressed_string
    return string

print(compress("aabcccccaaa"))
print(compress("abcca"))
