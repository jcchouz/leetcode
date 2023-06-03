import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        # 创建滑动窗口，哈希表
        hsmap = dict()

        # 遍历判断是否重复
        for i, c in enumerate(s):
            hsmap.pop(next(iter(hsmap.keys())))
            hsmap[i] = c
            res = max(res, len(hsmap))
        return res


if __name__ == '__main__':
    s = Solution()
    while True:
        print(s.lengthOfLongestSubstring(eval(input())))
