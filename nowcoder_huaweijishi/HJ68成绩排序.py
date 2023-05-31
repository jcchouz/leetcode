import traceback


while True:
    try:
        n = eval(input())
        flag = False if eval(input()) == 1 else True
        l = list()
        for _ in range(n):
            s = input().split(' ')
            l.append((s[0], int(s[1])))
        l.sort(key=lambda x: x[1], reverse=flag)
        for item in l:
            print(str(item[0] + ' ' + str(item[1])))
    except Exception as e:
        print(traceback.format_exc())
        break

'''
'''
