from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @return int整型
#
class Solution:
    def __init__(self) -> None:
        self.res = 0

    def mergeSort(self, data: List[int], l: int, r: int) -> None:
        m = (l + r) // 2
        if l < r:
            self.mergeSort(data, l, m)
            self.mergeSort(data, m + 1, r)
            self.merge(data, l, m, r)

    def merge(self, data: List[int], l: int, m: int, r: int) -> None:
        tmp = [-1] * (r - l + 1)
        tmp_idx = 0
        data_idx = l
        l2 = l
        r2 = m + 1
        while l2 <= m and r2 <= r:
            if data[l2] <= data[r2]:
                tmp[tmp_idx] = data[l2]
                l2 += 1
            else:
                self.res += m - l2 + 1
                self.res %= 1000000007
                tmp[tmp_idx] = data[r2]
                r2 += 1
            tmp_idx += 1
        while l2 <= m:
            tmp[tmp_idx] = data[l2]
            tmp_idx += 1
            l2 += 1
        while r2 <= r:
            tmp[tmp_idx] = data[r2]
            tmp_idx += 1
            r2 += 1
        for i in range(r - l + 1):
            data[data_idx] = tmp[i]
            data_idx += 1

    def InversePairs(self, data: List[int]) -> int:
        # write code here
        if len(data) < 2:
            return 0
        self.mergeSort(data, 0, len(data) - 1)
        return self.res
