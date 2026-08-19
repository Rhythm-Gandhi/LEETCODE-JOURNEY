class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            res =  n
        else:
            res = self.fib(n-1)+ self.fib(n-2)
        return res
        