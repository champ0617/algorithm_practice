"""
1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  （答案保证符合 32 位整数。）
"""


class Solution:
    def clumsy(self, N: int)-> int:
        """
        stack
        """

        index = 0
        stack = list()

        """
        fisrt multipy divide
        """
        for i in range(N, 0, -1):
            if stack:
                if index % 4 == 0:
                    value = stack.pop()
                    stack.append(value * i)
                elif index % 4 == 1:
                    value = stack.pop()
                    stack.append(value // i)
                else:
                    stack.append(i)
                index += 1
            else:
                stack.append(N)

        """
        add minus
        """
        for i in range(1, len(stack)):
            if i % 2:
                stack[i] = stack[i-1] + stack[i]
            else:
                stack[i] = stack[i-1] - stack[i]
        return stack.pop()


if __name__ == "__main__":

    s = Solution()
    print(s.clumsy(1))
