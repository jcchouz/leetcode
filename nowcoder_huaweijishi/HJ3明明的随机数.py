while True:
    try:
        n = int(input())
        l = list()
        for i in range(n):
            l.append(int(input()))
        l2 = sorted(set(l))
        for num in l2:
            print(num)
    except (EOFError, KeyboardInterrupt):
        break
