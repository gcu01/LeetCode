1class Solution(object):
2    def checkStraightLine(self, coordinates):
3        """
4        :type coordinates: List[List[int]]
5        :rtype: bool
6        """
7        if len(coordinates)<2:
8            return False
9        elif len(coordinates)==2:
10            return True
11
12        for i in range(2,len(coordinates)):
13            # x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
14            t1 = coordinates[i-2][0] * (coordinates[i-1][1]-coordinates[i][1])
15            t2 = coordinates[i-1][0] * (coordinates[i][1]-coordinates[i-2][1])
16            t3 = coordinates[i][0] * (coordinates[i-2][1]-coordinates[i-1][1])
17            if t1 + t2 + t3 != 0:      
18                return False
19        return True
20