1class Solution(object):
2    def numberOfAlternatingGroups(self, colors):
3        """
4        :type colors: List[int]
5        :rtype: int
6        """
7        out = 0
8        n = len(colors)-1
9        for i in range(1, n):
10            #print("colors[i]=", colors[i])
11            if colors[i-1] != colors[i] and colors[i] != colors[i+1]:
12                out += 1
13        
14        if colors[n-1] != colors[n] and colors[n] != colors[0]:
15            out += 1
16        if colors[n] != colors[0] and colors[0] != colors[1]:
17            out += 1
18        
19        return out