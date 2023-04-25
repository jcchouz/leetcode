#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param S string字符串
# @param T string字符串
# @return string字符串
#
class Solution:
    def check(self, hashmap: dict) -> bool:
        for _, value in hashmap.items():
            if value < 0:
                return False
        return True

    def minWindow(self, S: str, T: str) -> str:
        # write code here
        cnt = len(S) + 1
        hashmap = dict()
        for i in range(len(T)):
            if T[i] in hashmap:
                hashmap[T[i]] -= 1
            else:
                hashmap[T[i]] = -1
        slow = fast = 0
        l = r = -1
        while fast < len(S):
            if S[fast] in hashmap:
                hashmap[S[fast]] += 1
            while self.check(hashmap):
                if cnt > fast - slow + 1:
                    cnt = fast - slow + 1
                    l = slow
                    r = fast
                if S[slow] in hashmap:
                    hashmap[S[slow]] -= 1
                slow += 1
            fast += 1
        if l == -1:
            return ""
        return S[l : r + 1]


while True:
    try:
        # 输入输出
        strs = eval(input())
        # .strip().split(",")
        solution = Solution()
        res = solution.minWindow(strs[0], strs[1])
        print(res)
    except:
        print("error.")
        break
