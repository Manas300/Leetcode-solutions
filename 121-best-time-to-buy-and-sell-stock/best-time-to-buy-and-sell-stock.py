class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Start with a very high minimum price
        max_profit = 0  # Initialize maximum profit to 0

        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Calculate the profit and update the maximum profit
            max_profit = max(max_profit, price - min_price)

        return max_profit
        