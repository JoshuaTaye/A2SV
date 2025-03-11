# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(rowIndex):
            newRow = [1]
            for i in range(len(row) - 1):
                newRow.append(row[i] + row[i+1])
            newRow.append(1)
            row = newRow
        return row