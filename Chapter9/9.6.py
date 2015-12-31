memo = dict()

def get_paren_patterns(n):
    if n in memo:
        return memo[n]
    memo[n] = set()
    if n == 1:
        memo[n] = ["()"]
        return memo[n]
    patterns = get_paren_patterns(n - 1)
    for pattern in patterns:
        memo[n].add("()" + pattern)
        memo[n].add("(" + pattern + ")")
        memo[n].add(pattern + "()")
    return memo[n]


def main():
    for i in range(1, 5):
        print get_paren_patterns(i)

main()
