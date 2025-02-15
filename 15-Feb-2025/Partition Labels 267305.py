# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = defaultdict(str)
        for i in range(len(s)):
            hm[s[i]] = i
        end = 0
        size = 1
        arr = []
        for i in range(len(s)):
            end = max(end, hm[s[i]])
            if end == i:
                arr.append(size)
                size = 0
            size += 1

        return arr

        