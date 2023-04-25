from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxWater(self, arr: List[int]) -> int:
        # write code here
        res = 0
        if not len(arr):
            return res
        l = 0
        r = len(arr) - 1
        max_l = max_r = 0
        while l < r:
            max_l = max(max_l, arr[l])
            max_r = max(max_r, arr[r])
            if max_l < max_r:
                res += max_l - arr[l]
                l += 1
            else:
                res += max_r - arr[r]
                r -= 1
        return res


while True:
    try:
        # 输入输出
        arr = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.maxWater(arr)
        print(res)
    except Exception as e:
        print(e)
        break
