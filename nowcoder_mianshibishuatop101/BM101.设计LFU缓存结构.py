from collections import deque
import traceback
from typing import List


class Node:
    def __init__(self, key, val, freq) -> None:
        self.key = key
        self.val = val
        self.freq = freq


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# lfu design
# @param operators int整型二维数组 ops
# @param k int整型 the k
# @return int整型一维数组
#
class Solution:
    def __init__(self) -> None:
        # write code here
        self.capacity = 0
        self.hashmap = dict()
        self.freq_hsmp = dict(deque())
        self.min_freq = 0

    def update(self, node: Node, key: int, value: int) -> None:
        freq = node.freq
        self.freq_hsmp[freq].remove(node)
        if not len(self.freq_hsmp[freq]):
            self.freq_hsmp.pop(freq)
            if self.min_freq == freq:
                self.min_freq += 1
        node = Node(key, value, freq + 1)
        if freq + 1 not in self.freq_hsmp:
            self.freq_hsmp[freq + 1] = deque()
        self.freq_hsmp[freq + 1].appendleft(node)
        self.hashmap[key] = node

    def set(self, key: int, value: int) -> None:
        # write code here
        if key in self.hashmap:
            self.update(self.hashmap[key], key, value)
        else:
            if len(self.hashmap) == self.capacity:
                min_freq_node = self.freq_hsmp[self.min_freq].pop()
                if not len(self.freq_hsmp[self.min_freq]):
                    self.freq_hsmp.pop(self.min_freq)
                self.hashmap.pop(min_freq_node.key)
            node = Node(key, value, 1)
            self.min_freq = 1
            if 1 not in self.freq_hsmp:
                self.freq_hsmp[1] = deque()
            self.freq_hsmp[1].appendleft(node)
            self.hashmap[key] = node

    def get(self, key: int) -> int:
        # write code here
        if key in self.hashmap:
            node = self.hashmap[key]
            self.update(node, key, node.val)
            return node.val
        return -1

    def LFU(self, operators: List[List[int]], k: int) -> List[int]:
        # write code here
        res = []
        self.capacity = k
        for i in range(len(operators)):
            op = operators[i]
            if op[0] == 1:
                self.set(op[1], op[2])
            else:
                res.append(self.get(op[1]))
        return res


while True:
    try:
        # 输入输出
        operators, k = eval(input())
        # .strip().split(",")
        res = []
        solution = Solution()
        print(solution.LFU(operators, k))
    except Exception as e:
        print(traceback.format_exc())
        break
