class Solution:
    @classmethod
    def climbStairs(cls, n: int) -> int:
        if n == 1:
            return 1

        dp =  [None] * (n + 1)
        # dp=[]
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

print(Solution.climbStairs(6))