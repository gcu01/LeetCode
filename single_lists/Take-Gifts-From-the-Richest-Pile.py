1import math
2class Solution(object):
3    def pickGifts(self, gifts, k):
4        """
5        :type gifts: List[int]
6        :type k: int
7        :rtype: int
8        """
9        while k:
10            maxim = max(gifts)
11            idx = gifts.index(maxim)
12            #gifts[idx] = math.isqrt(maxim)
13            gifts[idx] = int(maxim ** 0.5)
14            k -= 1
15        return sum (gifts)