import traceback


while True:
    try:
        n = input()
        print(int(n, 16))
    except Exception as e:
        print(traceback.format_exc())
        break
