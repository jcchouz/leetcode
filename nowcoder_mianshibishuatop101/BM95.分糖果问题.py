from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# pick candy
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def candy(self, arr: List[int]) -> int:
        # write code here
        n = len(arr)
        nums = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                nums[i] = nums[i - 1] + 1
        i = n - 1
        while i > 0:
            if arr[i] < arr[i - 1] and nums[i] >= nums[i - 1]:
                nums[i - 1] = nums[i] + 1
            i -= 1
        return sum(nums)


while True:
    try:
        # 输入输出
        arr = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.candy(arr)
        print(res)
    except Exception as e:
        print(e)
        break
