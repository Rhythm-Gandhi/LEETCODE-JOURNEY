class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        n = len(nums)
        j = 0 
        maxl = 0
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            while freq[nums[i]]>k:
                freq[nums[j]] -= 1
                j +=1
                
            maxl = max(maxl,i-j+1)
        return maxl
