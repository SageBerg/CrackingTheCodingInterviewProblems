def sort_by_anagrams(arr):
    anagram_lists = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if is_anagram(arr[i], arr[j]):
                anagram

def is_anagram(string1, string2):
    return get_letter_counts(string1) == get_letter_counts(string2)

def get_letter_counts(string):
    counts = dict()
    for letter in string:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts
  
def main():
    print is_anagram("yayax", "xayay")
    print is_anagram("yaax", "xayay")

main()
