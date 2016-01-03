def bin_search(arr, target, offset):
    middle = len(arr) / 2
    if (len(arr) == 1 and arr[middle] != target) or \
       len(arr) < 1:
         return False
    if arr[middle] == target:
         return offset + middle
    if arr[middle] == "":
         return bin_search(arr[middle:], target, offset + middle) or \
                bin_search(arr[:middle], target, offset)
    if arr[middle] < target:
        return bin_search(arr[middle:], target, offset + middle)
    if arr[middle] > target:
        return bin_search(arr[:middle], target, offset)

def main():
    print bin_search( ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "at", 0)
    print bin_search( ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball", 0)
    print bin_search( ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "car", 0)
    print bin_search( ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "dad", 0)

main()

