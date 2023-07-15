from typing import List


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def binary_search(self, nums: List[int], target: int) -> bool:
        # write code here
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here
        if not array:
            return None
        for row in array:
            if self.binary_search(row, target):
                return True
        return False


# 20230715
