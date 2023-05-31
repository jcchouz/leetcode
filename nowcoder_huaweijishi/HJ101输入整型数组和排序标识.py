import traceback


while True:
    try:
        n = eval(input())
        l = list(map(int, input().split(" ")))
        flag = eval(input())
        flag = True if flag == 1 else False
        l.sort(reverse=flag)
        l = map(str, l)
        print(' '.join(l))
    except Exception as e:
        print(traceback.format_exc())
        break
