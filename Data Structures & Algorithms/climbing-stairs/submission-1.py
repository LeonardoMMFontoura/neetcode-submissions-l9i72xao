class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for degrau in range(3, n+1):
            dp[degrau] = dp[degrau-1] + dp[degrau-2]
        return dp[n]