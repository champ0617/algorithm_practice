from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n -1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        # merge_num = []
        # i = j = 0
        # while i <= m-1 and j <= n-1:
        #     if nums1[i] <= nums2[j]:
        #         merge_num.append(nums1[i])
        #         i = i + 1
        #     else:
        #         merge_num.append(nums2[j])
        #         j = j + 1
        # if i < m-1:
        #     while i <= m-1:
        #         merge_num.append(nums1[i])
        #         i += 1
        # else:
        #     while j <= n-1:
        #         merge_num.append(nums2[j])
        #         j += 1
        # print(merge_num)


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)


