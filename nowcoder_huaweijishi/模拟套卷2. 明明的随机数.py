import traceback


while True:
    try:
        n = int(input())
        l = list()
        for i in range(n):
            l.append(int(input()))
        res = sorted(set(l))
        for i in res:
            print(i)
    except Exception as e:
        print(traceback.format_exc())
        break
