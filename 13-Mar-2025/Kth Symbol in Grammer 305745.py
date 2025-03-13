# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, m: int, l: int) -> int:
        st = []
        def solve(n, k):
            if n == 1:
                return 0
            st.append(k)
            res = solve(n-1, k//2)
            x = st.pop()
            if not x % 2:
                return res
            else:
                return 1 - res
        return solve(m,l-1)



