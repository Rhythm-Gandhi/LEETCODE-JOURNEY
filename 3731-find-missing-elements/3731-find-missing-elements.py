class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        s = set(nums)
        lst = []
        for i in range(mn+1,mx):
            if i not in s:
               lst.append(i)
        return lst