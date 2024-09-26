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

Explanation from NeetCode:
https://www.youtube.com/watch?v=T41rL0L3Pnw 
NeetCode solution uses one less var, than from the author.

My ideas:
It can have multiple zeros?
Multiple rows & columns might be needed to be zeroed.

"""
import unittest
from copy import deepcopy

import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

from common_f import print_matrix


def zero_matrix1(matrix: list[list[int]]) -> list[list[int]]:
    """
    Brute force solution.
    Time complexity: O(M*N)
    Space complexity: O(M+N)

    This solution can be optimized.
    - create two arrays for zero cols and zero rows
    - iterate over both of them and convert rows and cols to zeroes

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
    
    # print("zero columns:", zero_columns)
    # print("zero_rows:", zero_rows)

    
    set_row_to_zero = False

    for i in range(len(matrix)):
        if i in zero_rows:  # this check can be switched to iteration over array
            set_row_to_zero = True

        set_column_to_zero = False
        for j in range(len(matrix[0])):
            if j in zero_columns:  # this check can be switched to iteration over array
                set_column_to_zero = True
            if set_column_to_zero or set_row_to_zero:
                matrix[i][j] = 0
            set_column_to_zero = False
        
        set_row_to_zero = False
    
    return matrix

def zero_matrix2(matrix: list[list[int]]) -> list[list[int]]:
    """
    Time complexity: O(N^2). Iterate every value in the matrix.
    Space complexity: O(1). Fixed amount for memory. 1 additional var + we use matrix itself.
    
    It is important in iterators to skip the index [0][0], because otherwise we will get
    incorrect results.
    """

    ROWS, COLS = len(matrix), len(matrix[0])

    # this variable is needed, since there is an intersection in the [0][0]
    # we use cell [0][0] to store information about first column, but not the first row
    row_zero = False

    # search for the zeroes
    # we start iterating from 0, but if there is a zero in [0][0],
    # store it in the separate variable
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                # save column
                matrix[0][c] = 0

                # save row
                if r > 0:  # avoid storing for the first row
                    matrix[r][0] = 0
                else:
                    row_zero = True

    # making columns zero
    for c in range(1, COLS):
        if matrix[0][c] == 0:
            for r in range(len(matrix)):
                matrix[r][c] = 0
    
    # making rows zero
    for r in range(1, ROWS):
        if matrix[r][0] == 0:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

    # convert first column
    if matrix[0][0] == 0:
        for i in range(ROWS):
            matrix[i][0] = 0

    # convert first row, if needed
    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0    

    return matrix

class TestRotateMatrix(unittest.TestCase):
    cases = [
        (
            [
                [1, 2, 3, 4],  # 1. no changes
                [5, 6, 7, 8], 
                [9, 10, 11, 12]
            ], 
            [
                [1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]
            ]
        ),
        (
            
            [
                [1, 2, 3, 4],  # 2. single zero 
                [5, 0, 6, 7], 
                [8, 9, 10, 11]
            ],
            [
                [1, 0, 3, 4],  
                [0, 0, 0, 0], 
                [8, 0, 10, 11]
            ]
        ),
        (
            [
                [1, 2, 3, 4],  # 3. two zeros
                [5, 0, 6, 7], 
                [8, 9, 10, 0]
            ],
            [
                [1, 0, 3, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]  
            ]
        ),
        (
            [
                [0, 1, 2, 3],  # 4. zero in the [0][0] cell
                [4, 5, 6, 7],
                [8, 9, 10, 11]
            ],
            [
                [0, 0, 0, 0],
                [0, 5, 6, 7],
                [0, 9, 10, 11]
            ]
        ),
        (
            [
                [1, 0, 2, 3],  # 5. zero in the first row
                [4, 5, 6, 7],
                [8, 9, 10, 11]
            ],
            [
                [0, 0, 0, 0], 
                [4, 0, 6, 7],
                [8, 0, 10, 11]
            ]
        ),
                (
            [
                [0, 0, 2, 3],  # 6. two zeros in the first row
                [4, 5, 6, 7],
                [8, 9, 10, 11]
            ],
            [
                [0, 0, 0, 0], 
                [0, 0, 6, 7],
                [0, 0, 10, 11]
            ]
        )
    ]

    functions = [
        zero_matrix1,
        zero_matrix2
    ]


    def test_rotate_matrix(self):
        for fun in self.functions:
            for matrix, result in self.cases:
                test_matrix = deepcopy(matrix)
                with self.subTest(input_data=test_matrix, expected=result):
                    self.assertEqual(fun(test_matrix), result)

if __name__ == "__main__":
    # comment this for simple tests
    unittest.main()

    # no zeros
    matrix_0 = [[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]]

    # single zero
    matrix_1 = [[1, 2, 3, 4], 
                [5, 0, 6, 7], 
                [8, 9, 10, 11]]
    
    # # two zeroes
    matrix_2 = [[1, 2, 3, 4], 
                [5, 0, 6, 7], 
                [8, 9, 10, 0]]
    
    # zero in the [0][0] cell
    matrix_3 = [[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]]
    
    # zero in the first row
    matrix_4 = [[1, 0, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]]

    # zero in the first row and first column
    matrix_5 = [[0, 0, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]]
    
    data = [matrix_0, matrix_1, matrix_2, matrix_3, matrix_4, matrix_5]

    for i, matrix in enumerate(data):
        print("i:", i)
        print_matrix(matrix)
        print_matrix(zero_matrix2(matrix))

