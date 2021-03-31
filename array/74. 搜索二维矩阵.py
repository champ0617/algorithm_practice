"""
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        """
        binary search 二分法
        """

        # special situation
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False

        # row binary
        start = 0
        end = len(matrix)
        while start < end - 1:
            mid = (start + end) // 2
            if matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] > target:
                end = mid
            else:
                return True
        row_mid = start

        # column binary
        start = 0
        end = len(matrix[0])
        while start < end:
            mid = (start + end) // 2
            if matrix[row_mid][mid] < target:
                start = mid
            elif matrix[row_mid][mid] > target:
                end = mid
            else:
                return True
            if start == end - 1:
                if (
                    matrix[row_mid][start] != target and
                    matrix[row_mid][end - 1] != target
                ):
                    return False
        return False


if __name__ == "__main__":
    matrix = [[1]]
    s = Solution()
    result = s.searchMatrix(matrix, 1)
    print(result)
