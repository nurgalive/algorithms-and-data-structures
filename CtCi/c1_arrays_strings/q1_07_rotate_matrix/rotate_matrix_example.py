def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)  # size of the matrix
    print("n:", n)
    print("layers:", n // 2)
    # iterate over layers. Starting the outermost layer, start=0
    # For example, in a 4x4 matrix:
    # For layer 0: first = 0, last = 3.
    # For layer 1: first = 1, last = 2.
    for layer in range(n // 2):  # getting layers (concentric "rings") to rotate
        first, last = layer, n - layer - 1
        print("first:", first)
        print("last:", last)
        print("layer:", layer)
        for i in range(first, last):
            # save top
            print("i:", i)

            top = matrix[layer][i]
            print("top:", top)

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]
            print_matrix(matrix)

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            print_matrix(matrix)

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            print_matrix(matrix)

            # top -> right
            matrix[i][-layer - 1] = top
            print_matrix(matrix)
    return matrix


def print_matrix(matrix: list):
    height = len(matrix)
    width = len(matrix[0])

    for h in range(height):
        print("")
        for w in range(width):
            print(matrix[h][w], end="\t")
    print("")

arr1 = [[i for i in range(j, j + 3)] for j in range(0, 9, 3)]
print_matrix(arr1)
print_matrix(rotate_matrix(arr1))



arr2 = [[i for i in range(j, j + 4)] for j in range(0, 16, 4)]
# print_matrix(arr2)

arr3 = [[1, 2, 3, 4, 5],   
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]

# print_matrix(arr1)

