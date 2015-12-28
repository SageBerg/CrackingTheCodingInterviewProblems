
def naive_find_pairs(array, target_sum):
    pairs = []
    for i in range(len(array)):
        if array[i] < target_sum:
            j = i + 1
            while j < len(array):
                if array[i] + array[j] == target_sum:
                    pairs.append((array[i], array[j]))
                j += 1
    return pairs

def find_pairs(array, target_sum):
    pairs = []
    hash_map = set()
    for number in array:
        if target_sum - number in hash_map:
            pairs.append((number, target_sum - number))
        if number not in hash_map:
            hash_map.add(number)
    return pairs

def main():
    print find_pairs([1, 2, 3, 4, 6, -1], 5)

main()
