# 题目11. 经过一次操作后的最大子数组和
# 你有一个整数数组 nums。你只能将一个元素 nums[i] 替换为 nums[i] * nums[i]。返回替换后的最大子数组和。
# 输入：nums = [2,-1,-4,-3]   输出：17
# 输入：nums = [1,-1,1,1,-1,-1,1]  输出：4
from typing import List

'''
nums[i]^2-nums[i]
'''


# 已知一点图，电路已有的原件包括电源，电阻，开关，导线。
# 电路中每根导线都有编号，要求给出算法，
# 任意输入电路图开关状态（0表示打开，1表示闭合）算法可以输出每根导线的电流情况，有电流流过为1，没有为2
# 输入：[1,1,1,1,1]
# 输出：['L0', 'k1', 'L1', 'L2', 'L3', 'k2', 'L4', 'L11', 'L10', 'L8', 'k4', 'L6', 'k3', 'L5', 'L7', 'k5', 'L9']

# 输入：[0,0,0,0,0]
# 输出：[]

# 输入：[0,1,1,1,1]
# 输出：[]

# 输入：[1,1,0,0,0]
# 输出：[]

# 要求该算法可以在其他电路图上套用


class Solution6:
    def maxSumAfterOperation(nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        res = float("-inf")
        dp = [[0] * (2) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0] + nums[i - 1], 0)
            dp[i][1] = max(dp[i - 1][1] + nums[i - 1], dp[i - 1][0] + nums[i - 1] ** 2)
            res = max(res, dp[i][1])
        return res
        pass


if __name__ == '__main__':
    nums = [2, -1, -4, -3]
    s = Solution6
    print(s.maxSumAfterOperation(nums))
