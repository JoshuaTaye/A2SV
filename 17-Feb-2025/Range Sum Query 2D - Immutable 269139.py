# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        tdps = [[0] * (len(matrix[0]) + 1), [0]]
        for j in range(len(matrix[0])):
            tdps[1].append(tdps[1][j] + matrix[0][j])
        for row in range(1, len(matrix)):
            tdps.append([0])
            tdps[row+1].append(tdps[row][1] + matrix[row][0])
            for col in range(1, len(matrix[0])):
                tdps[row+1].append(matrix[row][col] + tdps[row+1][col] + tdps[row][col+1] - tdps[row][col])
        self.tdps = tdps
    def sumRegion(self, row1, col1, row2, col2 ):
        return self.tdps[row2+1][col2+1] - self.tdps[row1][col2+1] - self.tdps[row2+1][col1] + self.tdps[row1][ col1]