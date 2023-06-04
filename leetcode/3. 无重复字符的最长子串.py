import collections


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         res = 0
#         # 创建滑动窗口，哈希表
#         hsmap = dict()
#
#         # 遍历判断是否重复
#         for i, c in enumerate(s):
#             hsmap.pop(next(iter(hsmap.keys())))
#             hsmap[i] = c
#             res = max(res, len(hsmap))
#         return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口，字典，计数
        lookup = collections.defaultdict(int)
        # end遍历
        start = end = 0
        max_len = 0
        while end < len(s):
            lookup[s[end]] += 1
            while lookup[s[end]] > 1:
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len


if __name__ == '__main__':
    s = Solution()
    while True:
        print(s.lengthOfLongestSubstring(eval(input())))
