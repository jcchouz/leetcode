import traceback

while True:
    try:
        n = int(input())
        m = list(map(int, input().split()))
        n = list(map(int, input().split()))
        fm = list()
        weight = set()
        weight.add(0)
        # 获取所有砝码
        for i in range(len(m)):
            for _ in range(n[i]):
                fm.append(m[i])
        # 遍历，set自动去重
        for i in fm:
            for j in weight.copy():
                weight.add(i + j)
        print(len(weight))
    except Exception as e:
        print(traceback.format_exc())
        break
