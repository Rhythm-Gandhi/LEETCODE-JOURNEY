class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        sett  = set()
        for i in range(n[0],n[-1]):
            if i not in n:
                sett.add(i)
            else:
                continue
        return sorted(list(sett))