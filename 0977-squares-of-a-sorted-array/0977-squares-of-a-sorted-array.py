class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0,len(nums),1):
            lst.append(nums[i]**2)
        return sorted(lst)
