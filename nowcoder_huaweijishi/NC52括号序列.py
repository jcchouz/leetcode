import traceback


while True:
    try:
        s = list(eval(input()))
        st = list()
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                st.append(c)
            else:
                if not st:
                    print(False)
                else:
                    if d[c] == st[-1]:
                        st.pop()
        print(not st)
    except Exception as e:
        print(traceback.format_exc())
        break

'''
'''
