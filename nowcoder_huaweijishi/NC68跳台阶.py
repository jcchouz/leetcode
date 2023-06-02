# import sys
#
# sys.setrecursionlimit(4000)
#
#
# def jumpFloor(number: int) -> int:
#     if number <= 1:
#         return 1
#     return jumpFloor(number - 1) + jumpFloor(number - 2)
#
#
# while True:
#     try:
#         n = eval(input())
#         print(jumpFloor(n))
#     except Exception as e:
#         print(e)
#         break


while True:
    try:
        num = int(input())
        if num <= 1:
            print(1)
        res = 0
        a, b = 1, 1
        for i in range(2, num + 1):
            res = a + b
            a = b
            b = res
        print(res)
    except:
        break
