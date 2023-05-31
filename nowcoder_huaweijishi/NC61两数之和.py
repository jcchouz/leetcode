while True:
    try:
        l, a = eval(input())
        res = list()
        hm = dict()
        for i in range(len(l)):
            tmp = a - l[i]
            if tmp not in hm:
                hm[l[i]] = i
            else:
                res.append(hm[tmp] + 1)
                res.append(i + 1)
                break
        print(res)
    except:
        break
