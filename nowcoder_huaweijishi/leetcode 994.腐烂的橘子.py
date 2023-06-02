# Definition for a binary tree node.
import queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 找邻居橘子
        def getNeighbor(x, y):
            l = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
            for a, b in l:
                if 0 <= a < row and 0 <= b < col:
                    yield a, b

        row = len(grid)
        col = len(grid[0])

        # 找0秒腐烂的橘子
        q = queue.Queue()
        for x, r in enumerate(grid):
            for y, val in enumerate(r):
                if val == 2:
                    q.put([x, y, 0])
        # 传染，使用BFS
        while q:
            x, y, t = q.get()
            for x2, y2 in getNeighbor(x, y):
                if grid[x2][y2] == 1:
                    grid[x2][y2] = 2
                    q.put([x2, y2, t + 1])

        if any(1 in row for row in grid):
            return -1

        return t


'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/rotting-oranges/solution/fu-lan-de-ju-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
