import traceback


while True:
    try:
        n = eval(input())
        hs = dict()
        for _ in range(n):
            s = input().split(' ')
            if s[0] not in hs:
                hs[[0]] = int(s[1])
            else:
                hs[s[0]] += int(s[1])
        for i in sorted(hs.keys()):
            print(str(i) + ' ' + str(hs[i]))
    except Exception as e:
        print(traceback.format_exc())
        break
