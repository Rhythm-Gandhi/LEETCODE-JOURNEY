class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if all(x==0 for x in nums):
            return 0
        tx = 0
        for i in nums:
            tx ^= i
        if tx != 0:
            return n
        return n-1