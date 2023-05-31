from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # write code here
        res = 0
        if len(height) < 2:
            return res
        l = 0
        r = len(height) - 1
        while l < r:
            capacity = min(height[l], height[r]) * (r - l)
            res = max(res, capacity)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


while True:
    try:
        # 输入输出
        arr = eval(input())
        # .strip().split(",")
        solution = Solution()
        # ip2num = solution.maxLength(arr)
        res = solution.maxArea(arr)
        print(res)
    except Exception as e:
        print(e)
        break
