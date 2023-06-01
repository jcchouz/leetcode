import traceback
from typing import Dict

while True:
    try:
        # 验证hashmap是否都>=0
        def check(hs: Dict) -> bool:
            for value in hs.values():
                if value < 0:
                    return False
            return True

        string = input().split(',')
        s = eval(string[0])
        t = eval(string[1])
        hs = dict()
        # hashmap存储负数
        for item in t:
            if item in hs:
                hs[item] -= 1
            else:
                hs[item] = -1
        # slow,fast扫描
        # l,r标记最小
        slow = fast = 0
        l = r = -1
        min_len = len(s)
        # fast扫描
        while fast < len(s):
            if s[fast] in hs:
                hs[s[fast]] += 1
            while check(hs):
                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    l = slow
                    r = fast
                if s[slow] in hs:
                    hs[s[slow]] -= 1
                slow += 1
            fast += 1
        # l==-1，一个都没找到
        if l == -1:
            print("")
        # 返回子串
        print(s[l : r + 1])
    except Exception as e:
        print(traceback.format_exc())
        break
