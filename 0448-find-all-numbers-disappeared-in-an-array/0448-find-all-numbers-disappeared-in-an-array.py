class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        seen = set(nums)
        for i in range(1,len(nums)+1,1):
            if i not in seen:
                lst.append(i)
        return lst
                


