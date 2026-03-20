1class Solution(object):
2    def isLongPressedName(self, name, typed):
3        """
4        :type name: str
5        :type typed: str
6        :rtype: bool
7        """
8        i, j = 0, 0
9        n, t = len(name), len(typed)
10
11        while j<t:
12            if i < n and name[i] == typed[j]:
13                i += 1
14            elif j == 0 or typed[j] != typed[j-1]:
15                return False
16            j += 1
17        return i == n
18
19        '''
20        j = 0
21        for i in range(len(typed)):
22            #print(" i = ", i, "   j=", j)
23            if typed[i] == name[j]:
24                if j < len(name)-1:
25                    j += 1
26                elif typed[i] * (len(typed)-i) == typed[i:]:
27                    return True
28                else:
29                    return False
30            elif i == 0 or i == (len(name)-1) or typed[i] != typed[i-1] or j == len(typed)-1 :
31                return False
32        return True
33        '''