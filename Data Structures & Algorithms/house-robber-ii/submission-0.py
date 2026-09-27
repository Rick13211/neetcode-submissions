class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(arr):
            m = len(arr)
            dp = [0] * (m + 1)

            dp[1] = arr[0]

            for i in range(2, m + 1):
                dp[i] = max(
                    dp[i - 2] + arr[i - 1],
                    dp[i - 1]
                )

            return dp[m]

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )