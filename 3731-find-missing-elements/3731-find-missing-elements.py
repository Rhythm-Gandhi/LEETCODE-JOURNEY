class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        lst = []
        for i in range(n[0],n[-1]):
            if i not in n:
                lst.append(i)
            else:
                continue
        return lst