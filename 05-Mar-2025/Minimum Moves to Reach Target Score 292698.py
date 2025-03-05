# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while maxDoubles > 0 and target > 1:
            if target % 2:
                moves += 1
            target = target // 2
            maxDoubles -= 1
            moves += 1
        if target > 1:
            moves += target - 1
        return moves