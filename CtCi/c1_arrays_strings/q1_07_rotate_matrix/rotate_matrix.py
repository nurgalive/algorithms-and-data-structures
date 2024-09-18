"""
Cracking the coding interview. Exercise 1.4. Page 91.

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Hints: #51, #100
#51 1.7. Try thinking about it layer by layer. Can you rotate a specific layer?
#100 1.7. Rotating a specific layer would just mean swapping the values in four arrays. If you were
asked to swap the values in two arrays, could you do this? Can you then extend it to four
arrays?

"""

def rotate_matrix(matrix: list[list[int]]) -> list:
    size = len(matrix)
    layers = size // 2
    # iterate over layers. Starting the outermost layer, start=0
    for layer in range(layers):
        # For example, in a 4x4 matrix:
        # For layer 0: first = 0, last = 3.
        # For layer 1: first = 1, last = 2.
        first_element_id = layer  # current layer
        last_element_id = size - layer - 1  # current layer
        for i in range(first_element_id, last_element_id):
            offset = i - first_element_id
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[last_element_id - offset][first_element_id]

    return matrix

def print_matrix(matrix: list):
    height = len(matrix)
    width = len(matrix[0])

    for h in range(height):
        print("")
        for w in range(width):
            print(matrix[h][w], end="\t")

if __name__ == "__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(input)
    # rotate_matrix(input)