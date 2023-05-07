from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # write code here
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return r
