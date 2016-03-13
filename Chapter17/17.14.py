dictionary = set()
dict_file = open("dict.txt")
for line in dict_file:
    dictionary.add(line.strip())


def unconcatenate(string, memo):
    if string in memo:
        return memo[string]
    for i in range(len(string)):
        for j in rnage(i, len(string)):
            if string[i:j] in dictionary:
                memo[i][j].append(string[i][j])

def naive_unconcatenate(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j] in dictionary:
                print string[i:j]

def main():
    test_case = "upona"
    memo = []
    for _ in range(len(test_case)):
         memo.append([[]] * len(test_case))
         
    naive_unconcatenate(test_case)


main()
