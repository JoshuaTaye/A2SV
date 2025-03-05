# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self):
        self.requests = []
    def ping(self, t):
        self.requests.append(t)
        requests = 0
        for i in range(len(self.requests)-1, -1, -1):
            if t - self.requests[i] <= 3000:
                requests += 1
            else:
                return requests
        return requests
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)