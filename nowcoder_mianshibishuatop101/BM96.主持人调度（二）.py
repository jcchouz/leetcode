from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算成功举办活动需要多少名主持人
# @param n int整型 有n个活动
# @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
# @return int整型
#
class Solution:
    def minmumNumberOfHost(self, n: int, startEnd: List[List[int]]) -> int:
        # write code here
        res = 0
        start = []
        end = []
        for tmp in startEnd:
            start.append(tmp[0])
            end.append(tmp[1])
        start.sort()
        end.sort()
        i = j = 0
        while j < n:
            if start[j] >= end[i]:
                i += 1
            else:
                res += 1
            j += 1
        return res


while True:
    try:
        # 输入输出
        args = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.minmumNumberOfHost(args[0], args[1])
        print(res)
    except Exception as e:
        print(e)
        break
