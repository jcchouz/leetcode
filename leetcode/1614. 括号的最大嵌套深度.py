import traceback


while True:
    try:
        s = list(eval(input()))
        st = list()
        d = {')': '(', ']': '[', '}': '{'}
        res = 0
        for c in s:
            if c in '([{':
                st.append(c)
                res = max(res, len(st))
            elif c in ')]}':
                st.pop()
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break

'''
'''
