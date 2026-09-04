class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        lst = []
        for i in range(n):
            a = max(nums[:i+1])
            b = min(nums[i:])
            c = a-b
            if c <= k:
                return i
        return -1


