class Solution:
    def countCommas(self, n: int) -> int:
        thresh = 1000
        res = 0
        while thresh <=n:
            res+= n-thresh+1
            thresh *=1000
        return res