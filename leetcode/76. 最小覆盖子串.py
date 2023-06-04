import collections


# class Solution:
#     def minWindow(self, s: 'str', t: 'str') -> 'str':
#         # 设置计数字典
#         lookup = collections.defaultdict(int)
#         # 存储每个目标字符的数量
#         for c in t:
#             lookup[c] -= 1
#         start, end = 0, 0
#         counter = -len(t)
#         min_len = float("inf")
#         res = ""
#         # end遍历
#         while end < len(s):
#             if lookup[s[end]] < 0:
#                 counter += 1
#             lookup[s[end]] += 1
#             # 包含所有，start左移
#             while not counter:
#                 if min_len > end - start + 1:
#                     min_len = end - start + 1
#                     res = s[start : end + 1]
#                 if lookup[s[start]] == 0:
#                     counter -= 1
#                 lookup[s[start]] -= 1
#                 start += 1
#             end += 1
#         return res
#
#

'''
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res

作者：powcai
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口，字典
        lookup = collections.defaultdict(int)
        # 每个目标字符单独计数
        for c in t:
            lookup[c] -= 1
        # end遍历
        start = 0
        counter = len(t)
        min_len = float("inf")
        res = ""
        for end, c in enumerate(s):
            if lookup[c] < 0:
                counter -= 1
            lookup[c] += 1
            # counter==0，找到所有
            while not counter:
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    res = s[start : end + 1]
                if not lookup[s[start]]:
                    counter += 1
                lookup[s[start]] -= 1
                start += 1
        return res


if __name__ == '__main__':
    s = Solution()
    while True:
        print(s.minWindow(eval(input()), eval(input())))
