def find_seq(array):
     min_sorted_seq_length = float("inf")
     location_of_shortest_seq = None
     for i in range(len(array)):
         for j in range(i, len(array)):
             if j - i > min_sorted_seq_length:
                 break
             start = array[0:i]
             middle = sorted(array[i:j])
             end = []
             if j + 1 < len(array):
		end = array[j+1:len(array)]
             if is_sorted(start + middle + end) and j - i < min_sorted_seq_length:
                min_sorted_seq_length = j - i
                location_of_shortest_seq = (i, j)
     return location_of_shortest_seq

def is_sorted(array):
    last_item = -float("inf")
    for item in array:
        if item < last_item:
            return False
        last_item = item
    return True  

def main():
    print find_seq([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])

main()
