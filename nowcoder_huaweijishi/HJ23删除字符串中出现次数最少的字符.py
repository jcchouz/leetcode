import traceback


while True:
    try:
        ip = list(map(int, input().split(".")))
        num = eval(input())
        ip2num = 0
        num2ip = ""
        for i in range(4):
            ip2num += ip[i] * pow(256, 3 - i)
        print(ip2num)
        for i in range(4):
            num2ip += str(num // pow(256, 3 - i)) + "."
            num = num % pow(256, 3 - i)
        print(num2ip[:-1])
    except Exception as e:
        print(traceback.format_exc())
        break
