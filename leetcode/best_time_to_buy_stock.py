class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        
        profit_max = 0
        min_price_so_far = float('inf')

        for index, price in enumerate(prices):
            

            if price < min_price_so_far:
                min_price_so_far = price

            if price > min_price_so_far:
                profit = price - min_price_so_far
                if profit > profit_max:
                    profit_max = profit 


        return profit_max
            
            



       

        

           
                