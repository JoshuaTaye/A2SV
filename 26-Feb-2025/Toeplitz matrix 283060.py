# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r = len(matrix)
        c =len(matrix[0])
        for row in range(1, r):
            for col in range(1, c):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
        return True
