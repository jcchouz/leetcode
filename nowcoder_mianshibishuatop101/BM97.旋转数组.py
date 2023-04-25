from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self, n: int, m: int, a: List[int]) -> List[int]:
        # write code here
        res = [0] * n
        for i in range(n):
            res[(i + m) % n] = a[i]
        return res


while True:
    try:
        # 输入输出
        args = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.solve(args[0], args[1], args[2])
        print(res)
    except Exception as e:
        print(e)
        break
