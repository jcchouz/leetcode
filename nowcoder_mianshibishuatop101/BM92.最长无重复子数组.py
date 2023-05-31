from typing import List
from collections import deque


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr: List[int]) -> int:
        # write code here
        res = 0
        if not len(arr):
            return res
        hashmap = dict()
        slow = fast = 0
        while fast < len(arr):
            if arr[fast] in hashmap:
                slow = max(slow, hashmap[arr[fast]] + 1)
            hashmap[arr[fast]] = fast
            res = max(res, fast - slow + 1)
            fast += 1
        return res

    def maxLength2(self, arr: List[int]) -> int:
        # write code here
        q = deque()
        res = 0
        for num in arr:
            while num in list(q):
                q.popleft()
            q.append(num)
            res = max(res, len(q))
        return res


while True:
    try:
        # 输入输出
        arr = eval(input())
        # .strip().split(",")
        solution = Solution()
        # ip2num = solution.maxLength(arr)
        res = solution.maxLength2(arr)
        print(res)
    except Exception as e:
        print(e)
        break
