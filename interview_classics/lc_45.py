from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) for i in range(len(nums))]
        dp[0] = 0

        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if i+j > len(nums) - 1:
                    break
                dp[i+j] = min(dp[i] + 1, dp[i+j])
        return dp[-1]



if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().jump(nums))
