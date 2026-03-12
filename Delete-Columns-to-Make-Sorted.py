1class Solution(object):
2    def minDeletionSize(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: int
6        """
7        out = 0
8        #print("a>b = ", "a"<"b")
9        
10        for i in range(len(strs[0])):
11            for j in range(1,len(strs)):
12                if strs[j-1][i] > strs[j][i]:
13                    out += 1
14                    break
15        return out
16
17        