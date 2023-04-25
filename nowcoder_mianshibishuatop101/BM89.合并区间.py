from typing import List


class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # write code here
        res = list()
        if not len(intervals):
            return res
        intervals.sort(key=lambda x: x.start)
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res


while True:
    try:
        # 输入输出
        lists = eval(input())
        intervals = list()
        for l in lists:
            intervals.append(Interval(l[0], l[1]))
        solution = Solution()
        res = solution.merge(intervals)
        print(res)
    except:
        print("error.")
        break
