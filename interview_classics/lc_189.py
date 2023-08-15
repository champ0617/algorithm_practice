from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = k % len(nums)
        nums[:] = nums[-m:] + nums[:-m]


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    print(nums[-2])
    Solution().rotate(nums, 3)
    print(nums)

