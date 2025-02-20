# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        ar = [0] * len(s)
        for i in shifts:
            if i[2] == 1:
                ar[i[0]] += 1
                if i[1]  < len(ar)-1:
                    ar[i[1]+1] -= 1
            else:
                ar[i[0]] -= 1
                if i[1]  < len(ar)-1:
                    ar[i[1]+1] += 1
        ps = [ar[0]]
        for i in range(1, len(ar)):
            ps.append(ar[i] + ps[i-1])
        for j in range(len(s)):
            curr = (ord(s[j]) - ord('a') + ps[j]) % 26
            s[j] = chr(curr + ord('a'))
        return ("".join(s))
