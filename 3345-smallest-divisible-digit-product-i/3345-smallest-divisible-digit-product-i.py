class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n, 1000):
            prod = 1
            for d in str(x):
                prod *= int(d)

            if prod % t == 0:
                return x
        
