# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        hm = {}
        def solve(l, r, t):
            if l > r:
                return 0
            elif (l, r, t) in hm:
                res = hm[(l, r, t)] 
            else:
                if t:
                    res = max(nums[l] + solve(l+1, r, False), nums[r] + solve(l, r - 1, False))
                else:
                    res = min(solve(l+1, r, True), solve(l, r-1, True))
                hm[(l, r, t)] = res
            return res
    
        turn = True
        fin = solve(0, len(nums)-1, turn)
        
        if fin < sum(nums) / 2:
            return False
        return True