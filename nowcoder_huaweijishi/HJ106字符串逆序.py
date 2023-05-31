import traceback


while True:
    try:
        s = input().replace(' ', '#')
        print(s[::-1].replace('#', ' '))
    except Exception as e:
        print(traceback.format_exc())
        break
