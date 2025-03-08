# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, arr: List[int]) -> bool:
        st = []
        minn = arr[0]
        for i in range(1, len(arr)):
            while st and arr[i] >= st[-1][0]:
                st.pop()
            if st and arr[i] > st[-1][-1]:
                return True
            st.append([arr[i], minn])
            minn = min(arr[i], minn)
        return False

        