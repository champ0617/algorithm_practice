"""
所有输入均为小写字母。
不考虑答案输出的顺序。
"""
import typing
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: typing.List[str]) -> typing.List[typing.List[str]]:
        """
        iter arr
        """

        result = defaultdict(list)
        for item in strs:
            item_list = list(item)
            item_list = sorted(item_list)
            item_str = "".join(item_list)
            result[item_str].append(item)
        return list(result.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
