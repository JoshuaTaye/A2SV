# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        stream = []
        self.stream = stream
        self.prefix = [[1]]
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix.append([1])
        else:
            self.prefix[-1].append((self.prefix[-1][-1])*num)
       
    def getProduct(self, k: int) -> int:
        res = 1
        if k >= len(self.prefix[-1]):
            return 0

        return ((self.prefix[-1][-1]) // (self.prefix[-1][len(self.prefix[-1])-k-1]))



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)