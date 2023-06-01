import traceback


def backtrace(index: int):
    if len(path) == k:
        res.append(path.copy())
        return
    for i in range(index, n):
        path.append(l[i])
        backtrace(i + 1)
        path.pop()


while True:
    try:
        s = input().split(',')
        n = int(s[0].split(' ')[-1])
        k = int(s[1].split(' ')[-1])
        l = list()
        for i in range(n):
            l.append(i + 1)
        res = list()
        path = list()
        backtrace(0)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
