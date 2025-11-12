class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        out = []
        maxim = max(candies)     
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxim:
                out.append(True)
            else:
                out.append(False)
        return out
        