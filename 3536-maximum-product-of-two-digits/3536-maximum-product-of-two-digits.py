class Solution:
    def maxProduct(self, n: int) -> int:
        lst = []
        for i in str(n):
            lst.append(int(i))
        x = sorted(lst)
        mul = x[-1]*x[-2]
        return mul


