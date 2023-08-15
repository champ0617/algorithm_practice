from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_crash = []
        dp_stock = []

        dp_crash.append(0)
        dp_stock.append(-prices[0])

        for i in range(1, len(prices)):
            dp_crash.append(max(dp_crash[i-1], dp_stock[i-1]+prices[i]))
            dp_stock.append(max(dp_stock[i-1], dp_crash[i-1]-prices[i]))
        return dp_crash[-1]

if __name__ == "__main__":
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))
