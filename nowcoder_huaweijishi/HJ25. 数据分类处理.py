import traceback


while True:
    try:
        I = input().split()[1:]
        R = sorted(set(map(int, input().split()[1:])))
        res = list()
        for r in R:
            r = str(r)
            tmp = list()
            for index, i in enumerate(I):
                if r in i:
                    tmp.extend([str(index), i])
            if tmp:
                res.extend([r, str(len(tmp) // 2)] + tmp)
        print(str(len(res)) + ' ' + ' '.join(res))

    except Exception as e:
        print(traceback.format_exc())
        break

'''
7 6396 4598 8539 6047 2019 11269 7402
3 16 4 26

12 4 3 1 4598 3 6047 6 7402 26 1 5 11269 
'''
