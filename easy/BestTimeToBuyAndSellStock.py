class Solution(object):
    def maxProfit(self, prices):
        profit=0
        l=0
        r=1
        while r< len(prices):
            current=prices[r]-prices[l]
            profit=max(profit, current)
            if prices[l] > prices[r]:
                l=r
            r+=1
        return profit
