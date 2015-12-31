memo = dict()

def get_coin_splits(n):
    if n in memo:
        return memo[n]
    if n == 0:
       return 1
    new_splits = 0
    for value in [1, 5, 10, 25]:
        if n >= value:
            new_splits += get_coin_splits(n - value)
    memo[n] = new_splits
    return new_splits

def main():
    for i in range(0, 200, 10):
        print get_coin_splits(i)

main()
