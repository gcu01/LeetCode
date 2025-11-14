class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range(len(prices)):            
            discount = 0
            k = i
            while k+1 < len(prices):
                if prices[k+1]<=prices[i]:
                    discount = prices[k+1]
                    break
                k += 1
            prices[i] = prices[i] - discount
        return prices