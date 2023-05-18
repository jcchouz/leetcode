#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # write code here
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]
