# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        hm = defaultdict(int)
        for i in range(len(nums2)):
            while s and nums2[i] > s[-1]:
                number = s.pop()
                hm[number] = nums2[i]
            s.append(nums2[i])
        ar = []
        for j in nums1:
            if j in hm:
                ar.append(hm[j])
            else:
                ar.append(-1)
        return ar
            

            

            