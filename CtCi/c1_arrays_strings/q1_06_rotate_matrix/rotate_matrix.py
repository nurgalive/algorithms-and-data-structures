"""
Cracking the coding interview. Exercise 1.4. Page 91.

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints:#51, # 100

"""

def rotate_matrix(matrix: list) -> list:
    height = len(matrix)
    width = len(matrix[0])
    result = []

    return list()

def print_martix(matrix: list):
    height = len(matrix)
    width = len(matrix[0])

    for h in range(height):
        print("")
        for w in range(width):
            print(matrix[h][w], end=" ")

if __name__ == "__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_martix(input)
    # rotate_matrix(input)