# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        placeholder = len(s) - 1
        s = list(s)
        seeker = 0
        sorteds = sorted(s)
        while sorteds != s:
            while s[placeholder] == "1":
                placeholder -= 1
            while s[seeker] == "0":
                seeker += 1
            swaps += placeholder - seeker
            s[seeker], s[placeholder] = s[placeholder], s[seeker]
            # placeholder -= 1
            # seeker += 1
        return swaps
