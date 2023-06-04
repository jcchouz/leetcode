# 计算最大乘积
# import traceback
#
#
# def compare(s1: str, s2: str):
#     if len(s1) > len(s2):
#         s1, s2 = s2, s1
#     for c in s1:
#         if c in s2:
#             return 0
#     return len(s1) * len(s2)
#
#
# while True:
#     try:
#         s = list(input().split(','))
#         res = 0
#         for i, s1 in enumerate(s):
#             for j, s2 in enumerate(s[i + 1 :]):
#                 res = max(res, compare(s1, s2))
#         print(res)
#     except Exception as e:
#         print(traceback.format_exc())
#         break

# 乱序数组中两数绝对值最小
# import traceback
#
# while True:
#     try:
#         l = list(map(int, input().split(' ')))
#         min_sum = float("inf")
#         hs = dict()
#         for i in range(len(l)):
#             for j in range(i + 1, len(l)):
#                 hs[abs(l[i] + l[j])] = [l[i], l[j]]
#         min_key = min(list(hs.keys()))
#         i, j = hs[min_key]
#         if i > j:
#             i, j = j, i
#         res = [str(i), str(j), str(abs(i + j))]
#         print(' '.join(res))
#     except Exception as e:
#         print(traceback.format_exc())
#         break

# 存储文件大小最大
import traceback

while True:
    try:
        n = int(input())
        tmp = list()
        for i in range(n):
            tmp.append(int(input()))
        # 重量
        wt = list()
        val = list()
        for i in range(n):
            if not tmp[i] % 512:
                wt.append(tmp[i] // 512)
            else:
                wt.append((tmp[i] // 512) + 1)
            val.append(tmp[i])
        chaju = 512
        for i in range(1, len(set(wt))):
            chaju = min(chaju, abs(wt[i] - wt[i - 1]))
        W = 1474560 // 512
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        val.sort()
        wt.sort()
        for i in range(1, n + 1):
            for w in range(min(wt), W + 1, chaju):
                if wt[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w - wt[i - 1]] + val[i - 1], dp[i - 1][w])
                    dp[i][w + 1 : w + chaju] = [dp[i][w] * (chaju - 1)]
        print(dp[n][W])
    except Exception as e:
        print(traceback.format_exc())
        break
