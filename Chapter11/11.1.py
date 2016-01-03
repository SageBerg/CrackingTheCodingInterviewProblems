def merge(arr1, arr2):
    merger = []
    index1 = 0
    index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            merger.append(arr1[index1])
            index1 += 1
        else:
            merger.append(arr2[index2])
            index2 += 1
    if index1 == len(arr1):
        merger += arr2[index2:]
    else:
        merger += arr1[index1:]      
    return merger

def main():
    print merge([1, 10, 20], [0, 5, 15, 100, 101])

main()
