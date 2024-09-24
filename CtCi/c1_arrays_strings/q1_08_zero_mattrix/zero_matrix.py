"""
Cracking the coding interview. Exercise 1.4. Page 91.

Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints:#17, #74, #102

#17. 1.8. If you just cleared the rows and columns as you found Os, you'd likely wind up clearing
the whole matrix. Try finding the cells with zeros first before making any changes to the
matrix.

#74 1.8. Can you use O(N) additional space instead of O(N^2)? What information do you really
need from the list of cells that are zero?

#102 1.8. You probably need some data storage to maintain a list of the rows and columns that
need to be zeroed. Can you reduce the additional space usage to 0(1) by using the
matrix itself for data storage?

LeetCode - https://leetcode.com/problems/set-matrix-zeroes/description/

Explanation:
https://www.youtube.com/watch?v=T41rL0L3Pnw 

My ideas:
It can have multiple zeros?
Multiple rows & columns might be needed to be zeroed.

"""
import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

from common_f import print_matrix

def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Brute force solution.
    Time complexity: O(N^2)
    Space complexity: O(N)

    i - row
    j - column
    """
    zero_columns = set()
    zero_rows = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    
    print("zero columns:", zero_columns)
    print("zero_rows:", zero_rows)

    
    set_row_to_zero = False

    for i in range(len(matrix)):
        if i in zero_rows:
            set_row_to_zero = True

        set_column_to_zero = False
        for j in range(len(matrix[0])):
            if j in zero_columns:
                set_column_to_zero = True
            if set_column_to_zero or set_row_to_zero:
                matrix[i][j] = 0
            set_column_to_zero = False
        
        set_row_to_zero = False
    
    return matrix
                

if __name__ == "__main__":
    matrix_1 = [[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 10, 11]]
    matrix_2 = [[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 10, 0]]
    print_matrix(matrix_1)
    print_matrix(zero_matrix(matrix_1))
    print_matrix(matrix_2)
    print_matrix(zero_matrix(matrix_2))


