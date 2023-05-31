import traceback


while True:
    try:
        n = eval(input())
        l = list()
        for _ in range(n):
            l.append(input())
        for i in sorted(l):
            print(i)
    except Exception as e:
        print(traceback.format_exc())
        break
