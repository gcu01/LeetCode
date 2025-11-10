class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out = []
        if n%2 != 0:
            out.append(0)
        add = 1
        while n//2 > 0:
           out.append(add)
           out.append(-add)
           add += 1
           n -= 2
        return out     
        