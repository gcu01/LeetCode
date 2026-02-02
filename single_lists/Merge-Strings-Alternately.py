1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        out = []
9        i, j = 0, 0
10        w1, w2 = list(word1), list(word2)
11        #print(w1)
12        #print(w2)
13        while i<len(w1) and j<len(w2):
14            out.append(w1[i])
15            out.append(w2[j])
16            i += 1
17            j += 1
18        if i<len(w1):
19            out += w1[i:]
20        if j<len(w2):
21            out += w2[j:]
22        #print(out)
23        return ''.join(out)
24        
25        