1class Solution(object):
2    def maximumUnits(self, boxTypes, truckSize):
3        """
4        :type boxTypes: List[List[int]]
5        :type truckSize: int
6        :rtype: int
7        """
8        boxTypes.sort(key=lambda x: x[1], reverse = True)
9        #print(boxTypes)
10        b,it = 0, 0
11        for box, item in boxTypes:
12            if box+b <= truckSize:
13                b += box
14                it += box * item
15            elif b < truckSize:                
16                it += (truckSize-b) * item                
17                break
18        return it
19
20
21
22