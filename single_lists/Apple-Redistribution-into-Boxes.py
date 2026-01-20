1class Solution(object):
2    def minimumBoxes(self, apple, capacity):
3        """
4        :type apple: List[int]
5        :type capacity: List[int]
6        :rtype: int
7        """
8        if sum(capacity) < sum(apple):
9            return 0
10        elif sum(capacity) == sum(apple):
11            return len(capacity)
12        
13        capacity.sort(reverse=True)
14        bck = capacity[:]
15        #print("initial capacity = ", capacity)
16        i, j = 0, 0
17        while i < len(apple) and j < len(capacity):
18            if apple[i] == capacity[j]:
19                capacity[j] = 0
20                i += 1
21                j += 1
22            elif apple[i] < capacity[j]:                
23                capacity[j] -= apple[i]
24                i += 1
25            else:
26                apple[i] -= capacity[j]
27                capacity[j] = 0
28                j += 1
29        #print("apple = ", apple)
30        #print("capacity =", capacity)
31        out = 0
32        for i in range(len(capacity)):
33            if bck[i] != capacity[i]:
34                out += 1
35            else:
36                break   
37        return out
38
39
40        '''
41        capacity.sort(reverse=True)
42        print("capacity=", capacity)
43        j = 0
44        op = 0
45        c = 0
46        bck = capacity[:]
47        print(bck)
48        for i in range(len(apple)):
49            c = capacity[j+1]
50            print("before capacity = ", capacity, "    c=", c, "   apple[i] =", apple[i])
51            
52            if apple[i] < capacity[j]:
53                print("apple=", apple[i])
54                capacity[j] -= apple[i]
55                print("c=", capacity)
56            #elif apple[i] == capacity[j]:
57            #    capacity[j] = 0
58            #    j += 1
59            #    op += 1
60            else:
61                capacity[j+1] -= abs(apple[i]-capacity[j])
62                capacity[j] = 0
63                c = capacity[j+1]
64                j += 1
65                op += 1
66                print(" next j = ", j)
67        print("end capacity = ", capacity, "    c=", c, "   bck=", bck)
68        print("bck[j] = ", bck[j])
69        out = 0
70        for i in range(len(bck)):
71            if bck[i] != capacity[i]:
72                out += 1
73        #return capacity.count(0) +1 if bck[j] != capacity[j] else capacity.count(0)
74        return out
75        '''