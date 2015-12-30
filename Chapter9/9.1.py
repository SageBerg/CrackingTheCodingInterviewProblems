memo = dict()

def count_ways(steps, ways):
    if steps in memo:
        return memo[steps]
    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    new_ways = 0
    new_ways += count_ways(steps - 1, ways)
    new_ways += count_ways(steps - 2, ways)
    new_ways += count_ways(steps - 3, ways)
    memo[steps] = ways + new_ways
    return ways + new_ways

def main():
   for i in range(1, 100):
       print count_ways(i, 0)

main()

