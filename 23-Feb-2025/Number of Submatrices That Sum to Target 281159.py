# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
            count = 0
            for r1 in range(len(matrix)):
                col_sums = [0] * len(matrix[0])
                for r2 in range(r1, len(matrix)):
                    for c in range(len(matrix[0])):
                        col_sums[c] += matrix[r2][c]
                    ps = defaultdict(int)
                    ps[0] = 1
                    cs = 0
                    for i in col_sums:
                        # print(i)
                        cs += i
                        count += ps[cs - target]
                        ps[cs] += 1
            return count