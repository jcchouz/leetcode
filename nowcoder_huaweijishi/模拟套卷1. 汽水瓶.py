import traceback


while True:
    try:
        n = eval(input())
        res = 0
        while n > 2:
            res += n // 3
            n = n % 3 + n // 3
        if n % 3 == 2:
            res += 1
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
