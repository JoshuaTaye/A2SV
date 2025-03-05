# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        repo = {5:0, 10:0, 20:0}
        n = len(bills)
        for i in range(n):
            if bills[i]== 5:
                repo[5] += 1
            elif bills[i] == 10 and repo[5] > 0:
                repo[5] -= 1
                repo[10] += 1
            elif bills[i] == 20 and repo[10] > 0 and repo[5] > 0 or repo[5] > 2:
                repo[20] += 1
                if repo[10] > 0 and repo[5] > 0:
                    repo[5] -= 1
                    repo[10] -= 1
                elif repo[5] > 2:
                    repo[5] -= 3
                else:
                    return False  
            else:
                return False
        return True
        
