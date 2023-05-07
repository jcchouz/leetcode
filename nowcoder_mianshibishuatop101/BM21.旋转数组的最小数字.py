from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param rotateArray int整型一维数组
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
        # write code here
        if not rotateArray:
            return None
        l, r = 0, len(rotateArray) - 1
        while l < r:
            m = (l + r) // 2
            if rotateArray[m] < rotateArray[r]:
                r = m
            elif rotateArray[m] > rotateArray[r]:
                l = m + 1
            else:
                r -= 1
        return rotateArray[l]
