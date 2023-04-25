from collections import OrderedDict


class Solution:
    def __init__(self, capacity: int):
        # write code here
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def set(self, key: int, value: int) -> None:
        # write code here
        if key in self.lru_cache:
            self.lru_cache.pop(key)
        self.lru_cache[key] = value
        if len(self.lru_cache) > self.capacity:
            self.lru_cache.popitem(last=False)

    def get(self, key: int) -> int:
        # write code here
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
        return self.lru_cache.get(key, -1)


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class Solution2:
    def __init__(self, capacity: int):
        # write code here
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hashmap = dict()

    def insertFirst(self, node: Node):
        node.pre = self.head
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node

    def moveToHead(self, node: Node):
        if node.pre == self.head:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        self.insertFirst(node)

    def removeLast(self, node: Node):
        self.hashmap.pop(self.tail.pre.key)
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre

    def set(self, key: int, value: int) -> None:
        # write code here
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.moveToHead(self.hashmap[key])
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.insertFirst(node)
            if len(self.hashmap) > self.capacity:
                self.removeLast(node)

    def get(self, key: int) -> int:
        # write code here
        if key in self.hashmap:
            self.moveToHead(self.hashmap[key])
            return self.hashmap[key].val
        return -1


# Your Solution object will be instantiated and called as such:
# solution = Solution(capacity)
# output = solution.get(key)
# solution.set(key,value)

while True:
    try:
        # 输入输出
        operators, nums, capacity = eval(input())
        # .strip().split(",")
        res = []
        solution = Solution2(capacity)
        # 遍历所有操作
        for i in range(len(operators)):
            if operators[i] == "set":
                # set操作
                solution.set(nums[i][0], nums[i][1])
                res.append("null")
            else:
                # get操作
                res.append(str(solution.get(nums[i][0])))
        print(res)
    except Exception as e:
        print(e)
        break
