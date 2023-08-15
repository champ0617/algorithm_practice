from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max:
        #             max = prices[j] - prices[i]
        # return max

        max_gap = 0
        min = max = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = max = prices[i]
            if prices[i] > max:
                max = prices[i]
                if max - min > max_gap:
                    max_gap = max - min
        return max_gap


if __name__ == "__main__":
    prices = [5, 4, 1, 2, 3]
    print(Solution().maxProfit(prices))
