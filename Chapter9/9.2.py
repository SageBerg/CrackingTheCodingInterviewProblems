memo = dict()

def count_paths(x, y, paths):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == y == 1:
        return 1
    new_paths = 0
    if x > 0:
       new_paths += count_paths(x - 1, y, paths)
    if y > 0:
       new_paths += count_paths(x, y - 1, paths)
    memo[(x, y)] = paths + new_paths
    return paths + new_paths

def main():
    for i in range(100):
        print count_paths(i, i, 0)

main()
