#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self, str: str) -> str:
        # write code here
        ans = ""
        for i in range(len(str)):
            ans += str[len(str) - 1 - i]
        return ans

    def solve2(self, str: str) -> str:
        # write code here
        return str[::-1]


while True:
    try:
        # 输入输出
        str = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.solve(str)
        print(res)
    except:
        print("error.")
        break
