import traceback


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
