"""
1 <= nums.length <= 3 * 10*4
-10*4 <= nums[i] <= 10*4
nums 已按升序排列
"""
import typing
from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: typing.List[int]) -> int:
        """
        先记录需要移除数值的index
        然后反向去删除这些数值
        """

        remove_index_list = []
        value_cnt = defaultdict(int)
        for i, num in enumerate(nums):
            if value_cnt.get(num):
                if value_cnt[num] + 1 > 2:
                    remove_index_list.append(i)
                else:
                    value_cnt[num] += 1
            else:
                value_cnt[num] = 1

        # reverse remove_index_list
        remove_index_list.reverse()
        for index in remove_index_list:
            nums.pop(index)
        return len(nums)


if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    s = Solution()
    data_len = s.removeDuplicates(nums)
    print(data_len)
    print(nums)