import traceback


while True:
    try:
        s = input().split()
        a = int(s[0])
        b = int(s[1])
        sum = a * b
        if a < b:
            a, b = b, a
        c = b % a
        while c:
            b, a = a, c
            c = b % a
        print(sum // a)
    except Exception as e:
        print(traceback.format_exc())
        break
