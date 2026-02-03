from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]   # buy on day 0

        for i in range(1, len(prices)):
            price = prices[i]

            new_cash = max(cash, hold + price - fee)  # sell or do nothing
            new_hold = max(hold, cash - price)        # buy or do nothing

            cash, hold = new_cash, new_hold

        return cash
