#As we scan the array from left to right, we keep track of the lowest price seen so far (mini).
#For each price, we calculate the profit we'd make if we sold today:
#profit = current_price - mini
#We continuously update the maximum profit found so far.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=prices[0]
        maxprofit=0
        for i in prices:
            if i<mini:
                mini = i
            profit = i -mini
            if profit>maxprofit:
                maxprofit = profit

        return maxprofit