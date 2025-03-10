# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minn = deque()
        maxx = deque()
        max_len = 0
        left = 0
        for right in range(len(nums)):
            while minn and nums[right] < minn[-1][0]:
                minn.pop()
            minn.append((nums[right], right))
            while maxx and nums[right] > maxx[-1][0]:
                maxx.pop()
            maxx.append((nums[right], right))
            while maxx and minn and maxx[0][0] - minn[0][0] > limit:
                if maxx and maxx[0][1] == left:
                    maxx.popleft()
                if minn and minn[0][1] == left:
                    minn.popleft()
                left += 1

            max_len = max(right - left + 1, max_len)
        return max_len

