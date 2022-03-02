"""
z字变换
"""
import time

import numpy as np
from functools import wraps


def time_decorate(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        data = func(*args, **kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return data
    return deco


class Solution(object):
    @time_decorate
    def convert(self, s: str, numRows: int) -> str:
        # generate transform matrix
        transform_matrix = []
        if numRows == 1:
            return s
        transform_matrix.extend([(1, 0)]*(numRows-1))
        transform_matrix.extend([(-1, 1)]*(numRows-1))

        init_matrix = [[''] * 1000 for i in range(1000)]
        init_matrix[0][0] = s[0]
        cur_x = 0
        cur_y = 0
        for i in range(len(s)-1):
            x_split = transform_matrix[i % len(transform_matrix)][0]
            y_split = transform_matrix[i % len(transform_matrix)][1]
            cur_x = cur_x + x_split
            cur_y = cur_y + y_split
            init_matrix[cur_x][cur_y] = s[i+1]
        row_join_data = ["".join(item) for item in init_matrix]
        join_data = "".join(row_join_data)
        return join_data


class Solution2(object):
    @time_decorate
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cur_row = 0
        init_matrix = [''] * numRows
        for i in range(len(s)):
            init_matrix[cur_row] += s[i]
            cur_row = cur_row - 1 if i % (2 * numRows - 2) >= numRows - 1 else cur_row + 1
        join_data = "".join(init_matrix)
        return join_data


if __name__ == "__main__":
    s = "AB"
    print(Solution2().convert(s, 1))
