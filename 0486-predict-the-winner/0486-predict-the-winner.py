class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                take_left = nums[i] - dp[j]
                take_right = nums[j] - dp[j - 1]
                dp[j] = max(take_left, take_right)
        return dp[n - 1] >= 0