import math
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_num = math.ceil(len(nums) / 2)
        data = {}
        for i in range(len(nums)):
            if nums[i] not in data.keys():
                data[nums[i]] = 1
            else:
                data[nums[i]] += 1
            if data[nums[i]] >= major_num:
                return nums[i]

if __name__ == "__main__":
    nums = [3,2,3]
    print(Solution().majorityElement(nums))