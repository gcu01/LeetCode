class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        distinct = set(candyType)
        if (len(candyType)/2) < len(distinct):
            return len(candyType)/2
        return len(distinct)
        