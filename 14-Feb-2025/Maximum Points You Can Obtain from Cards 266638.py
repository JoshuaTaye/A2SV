# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        p = n - k
        min_sum = 0
        i = 0
        while i < p:
            min_sum += cardPoints[i]
            i += 1
        left  = 0
        right = i
        curr_sum = min_sum
        for right in range(i, n):
            curr_sum = curr_sum - cardPoints[left] + cardPoints[right]
            min_sum = min(min_sum, curr_sum)
            left += 1
        return sum(cardPoints) - min_sum
