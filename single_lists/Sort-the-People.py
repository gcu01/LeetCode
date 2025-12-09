1class Solution(object):
2    def sortPeople(self, names, heights):
3        """
4        :type names: List[str]
5        :type heights: List[int]
6        :rtype: List[str]
7        """
8        tall = dict()
9        for i in range(len(names)):
10            #print("i = ", i)
11            tall[heights[i]] = names[i]
12        #print(tall)
13        heights.sort(reverse = True)
14        for i in range(len(heights)):
15            names[i] = tall[heights[i]]
16        #print(names)
17        #s = sorted(tall.items(), reverse=True))
18        #s = dict(sorted(tall.items(), key=lambda x: x[1], reverse=True))
19        #s = dict(sorted(tall.items(), reverse=True))
20        #print("sorted s=", s)
21        return names