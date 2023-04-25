while True:
    try:
        nums = list(map(int, input().strip().split(' ')))
        print(sum(nums))
    except:
        break
