from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param mat int整型二维数组
# @param n int整型
# @return int整型二维数组
#
class Solution:
    def rotateMatrix(self, mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        res = list()
        mat = list(zip(*mat))
        for i in range(n):
            res.append(list(mat[i][::-1]))
        return res

    def rotateMatrix2(self, mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        for i in range(n):
            for j in range(i):
                if i != j:
                    tmp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = tmp
        for i in range(n):
            mat[i].reverse()
        return mat


while True:
    try:
        # 输入输出
        args = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.rotateMatrix2(args[0], args[1])
        print(res)
    except Exception as e:
        print(e)
        break
