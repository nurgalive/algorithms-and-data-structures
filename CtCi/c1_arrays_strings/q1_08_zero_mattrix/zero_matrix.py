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

"""

def zero_matrix(matrix: list[list[int]]) -> None:
    pass

if __name__ == "__main__":
    zero_matrix(list())