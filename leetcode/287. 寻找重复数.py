from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    s = Solution()
    print(s.findDuplicate(nums))
