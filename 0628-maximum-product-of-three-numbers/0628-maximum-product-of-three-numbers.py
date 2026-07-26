class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        x = sorted(nums)
        op1 = x[-1]*x[-2]*x[-3]
        op2 = x[-1]*x[0]*x[1]
        return max(op1,op2)
     
        