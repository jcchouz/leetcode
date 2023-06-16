import traceback


def backtrace(i: int):
    if len(path) == len(s):
        res.append("".join(path))
        return
    for j in range(len(s)):
        if s[j] == '#' or (j > 0 and s[j] == s[j - 1]):
            continue
        path.append(s[j])
        s[j] = '#'
        backtrace(i + 1)
        s[j] = path.pop()


while True:
    try:
        s = sorted(input().split(' ')[2][1:-1])
        res = list()
        path = list()
        backtrace(0)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break

'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        S  = sorted(S)
        def backtrace(index):
            if len(path) == len(S):
                res.append("".join(path))
                return 
            for i in range(len(S)):
                if S[i] == 0:
                    continue 
                if S[i] == S[i-1] and i > 0:
                    continue
                path.append(S[i])
                S[i] = 0
                backtrace(index+1)
                S[i] = path.pop()
        path = []
        res = []
        backtrace(0)
        return res

作者：westqi
链接：https://leetcode.cn/problems/permutation-ii-lcci/solution/you-zhong-fu-zi-fu-chuan-de-pai-lie-zu-h-bxyi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
