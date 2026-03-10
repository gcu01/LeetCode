1class Solution(object):
2    def shortestCompletingWord(self, licensePlate, words):
3        """
4        :type licensePlate: str
5        :type words: List[str]
6        :rtype: str
7        """
8        l = "".join(c for c in licensePlate if not c.isdigit()).replace(" ","").lower()
9        #print("l=", l)
10        words = sorted(words, key = len)
11        #print("words = ", words)
12        for w in words:
13            for i in range(len(l)):
14                if w.count(l[i]) < l.count(l[i]):
15                    break
16                if i == (len(l) - 1):
17                    return w
18        return ""