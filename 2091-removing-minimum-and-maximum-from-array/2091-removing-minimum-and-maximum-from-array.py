class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi= nums.index(min(nums))
        ma = nums.index(max(nums))
        left = min(mi,ma)
        right = max(mi,ma)
        front = right+1
        back = len(nums) -left
        both = (left+1)+(len(nums)-right)
        moves = min(front,back,both)
        return moves