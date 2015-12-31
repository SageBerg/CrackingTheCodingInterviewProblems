def find_by_row(element, grid):  
    row_middle = len(grid) / 2
    col_middle = len(grid[0]) / 2
    if grid[row_middle][col_middle] == element:
        return True
    if grid[row_middle][col_middle] < element and len(grid) > 1:
        return find_by_row(element, grid[row_middle:])
    if grid[row_middle][col_middle] > element and len(grid) > 1:
        return find_by_row(element, grid[:row_middle])
    return find_by_col(element, grid[row_middle])

def find_by_col(element, row):
    middle = len(row) / 2
    if row[middle] == element:
        return True
    if row[middle] < element and len(row) > 1:
        return find_by_col(element, row[middle:])
    if row[middle] > element and len(row) > 1:
        return find_by_col(element, row[:middle])
    return False

def main():
    grid = [ [1, 2, 3, 4, 5],
             [2, 3, 4, 5, 6],
             [3, 4, 5, 6, 7],
             [4, 5, 6, 7, 8],
             [5, 6, 7, 8, 9],
             [6, 7, 8, 9, 10] ]
    for i in range(12):
    	print i, find_by_row(i, grid) 

main()
