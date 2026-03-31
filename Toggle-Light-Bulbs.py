1class Solution(object):
2    def toggleLightBulbs(self, bulbs):
3        """
4        :type bulbs: List[int]
5        :rtype: List[int]
6        """
7        b = Counter(bulbs)
8        #print("b=", b)
9        out = []
10        for bulb, c in b.items():            
11            if c%2 == 1:
12                out.append(bulb)
13        out.sort()
14        return out