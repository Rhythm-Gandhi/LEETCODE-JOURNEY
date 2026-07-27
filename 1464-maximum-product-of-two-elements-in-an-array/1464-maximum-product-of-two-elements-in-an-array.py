class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 0 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x = (nums[i]-1)*(nums[j]-1)
                maxi = max(maxi,x)
        return maxi
