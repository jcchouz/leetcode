import math
import traceback


# 验证是否为质数
def check(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


while True:
    try:
        # 输入
        num = eval(input())
        # 循环，中间向外扩张，检查是否都为质数
        for i in range(num // 2, 0, -1):
            if check(i) and check(num - i):
                print(i)
                print(num - i)
                break
    except Exception as e:
        print(traceback.format_exc())
        break
