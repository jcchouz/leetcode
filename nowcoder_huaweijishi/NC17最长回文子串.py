import traceback


# while True:
#     try:
#         s = eval(input())
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         res = 0
#         for length in range(1, n + 1):
#             for i in range(0, n - length + 1):
#                 j = i + length - 1
#                 if s[i] == s[j]:
#                     if length < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                     if dp[i][j]:
#                         res = max(res, length)
#         print(res)
#     except Exception as e:
#         print(traceback.format_exc())
#         break


def judge(s: str, l: int, r: int):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1


while True:
    try:
        s = eval(input())
        n = len(s)
        res = 0
        for i in range(n):
            tmp = max(judge(s, i, i), judge(s, i, i + 1))
            res = max(res, tmp)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
