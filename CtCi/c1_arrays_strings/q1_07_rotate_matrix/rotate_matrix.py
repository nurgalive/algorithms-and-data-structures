"""
Cracking the coding interview. Exercise 1.4. Page 91.

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Hints: #51, #100
#51 1.7. Try thinking about it layer by layer. Can you rotate a specific layer?
#100 1.7. Rotating a specific layer would just mean swapping the values in four arrays. If you were
asked to swap the values in two arrays, could you do this? Can you then extend it to four
arrays?

This problem is very hard to me.
Those many indexes drives me crazy.

Amazing explanation.
https://www.youtube.com/watch?v=fMSJSS7eO1w

"""
class Question:
    """
    In place update of the matrix.
    """
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def rotate_matrix(self) -> bool:
        """
        Time complexity: O(N^2)
        Space complexity: O(1)
        """
        for i in range(len(self.matrix)):
            if len(self.matrix) != len(self.matrix[i]):
                return False
            
        size = len(self.matrix)
        layers = size // 2
        # iterate over layers. Starting the outermost layer, start=0
        for layer in range(layers):
            # For example, in a 4x4 matrix:
            # For layer 0: first = 0, last = 3.
            # For layer 1: first = 1, last = 2.
            left = layer  # current layer
            right = size - 1 - layer  # current layer
            for i in range(left, right):
                offset = i - left
                top = self.matrix[left][i]

                # left -> top
                self.matrix[left][i] = self.matrix[right - offset][left]

                # bottom -> left
                self.matrix[right - offset][left] = self.matrix[right][right - offset]

                # right -> bottom
                self.matrix[right][right - offset] = self.matrix[i][right]

                # top -> right
                self.matrix[i][right] = top

        return True

    def print_matrix(self):
        for i in range(len(self.matrix)):
            if len(self.matrix) != len(self.matrix[i]):
                return False
        height = len(self.matrix)
        width = len(self.matrix[0])

        for h in range(height):
            print("")
            for w in range(width):
                print(self.matrix[h][w], end="\t")
        
        print("")
        return True
    


if __name__ == "__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    q = Question(input)
    q.print_matrix()
    q.rotate_matrix()
    q.print_matrix()