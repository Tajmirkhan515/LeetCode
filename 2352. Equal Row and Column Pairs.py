#2352. Equal Row and Column Pairs
#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


class Solution(object):
    def equalPairs(self, grid):
               
        row_count = {}

        # Store each row in the dictionary as a tuple (tuple as a key, and frequency as a value) e.g{(2,7,7):1}
        for row in grid:
            
            row_tuple = tuple(row)
            
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1

        
        count = 0
        n = len(grid)
        #iterate column
        for col in range(n):
            # Construct the current column as a tuple
            column_tuple = tuple(grid[row][col] for row in range(n))
            
            # If this column matches any row, add the count of that row
            if column_tuple in row_count:
                count =count+row_count[column_tuple]
        
        return count
                
