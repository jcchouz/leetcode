import traceback


while True:
    try:
        s = input()
        res = ""
        hsmap = dict()
        for c in s:
            if c not in hsmap:
                hsmap[c] = 1
            else:
                hsmap[c] += 1
        tmp = min(hsmap.values())
        for c in s:
            if hsmap[c] != tmp:
                res += c
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
