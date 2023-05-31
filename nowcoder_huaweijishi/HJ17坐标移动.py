import traceback


def check(s: str):
    if len(s) <= 8:
        return False
    check = [0] * 4
    for c in s:
        if c.isupper():
            check[0] = 1
        elif c.islower():
            check[1] = 1
        elif c.isdigit():
            check[2] = 1
        else:
            check[3] = 1
    if sum(check) < 3:
        return False
    for i in range(len(s) - 3):
        if s[i : i + 3] in s[i + 3 :]:
            return False
    return True


while True:
    try:
        s = input()
        if check(s):
            print("OK")
        else:
            print("NG")
    except Exception as e:
        print(traceback.format_exc())
        break
