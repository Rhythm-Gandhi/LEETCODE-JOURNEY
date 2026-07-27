class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 0 
        s = 0 
        for i in nums:
            if i >l:
                s = l
                l = i
                
            elif i>s:
                s = i 
        return (l-1)*(s-1)
