#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算两个数之和
# @param item string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#


class Solution:
    def solve(self, s: str, t: str) -> str:
        # write code here
        if len(s) == 0:
            return t
        if len(t) == 0:
            return s
        if len(s) < len(t):
            s, t = t, s
        carry = 0
        i = len(s) - 1
        while i >= 0:
            j = i - len(s) + len(t)
            temp = ord(s[i]) - ord("0") + carry
            if j >= 0:
                temp += ord(t[j]) - ord("0")
            carry = temp // 10
            temp = temp % 10
            s = s[:i] + str(temp) + s[i + 1 :]
            i -= 1
        if carry == 1:
            s = "1" + s
        return s


if __name__ == "__main__":
    while True:
        try:
            strs = input().strip().split(",")
            args = [strs[0][1:-1], strs[1][1:-1]]
            solution = Solution()
            res = solution.solve(*args)
            print(res)
        except:
            break
