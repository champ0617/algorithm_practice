from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_pos = 0
        for i in range(0, len(nums)-1):
            if max_pos < i:
                return False
            pos = nums[i] + i
            if pos > max_pos:
                max_pos = pos

            if pos >= len(nums)-1:
                return True
        return False


if __name__ == "__main__":
    nums = [0,2,3]
    print(Solution().canJump(nums))