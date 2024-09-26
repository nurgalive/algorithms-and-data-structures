"""
Set of common functions used between tasks.

"""

def print_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print("")
    print("")