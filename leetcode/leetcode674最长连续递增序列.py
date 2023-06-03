import traceback


while True:
    try:
        s = input().split(' ')
        l = eval(s[2])
        if not l:
            print(0)
        res = 1
        cnt = 1
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
