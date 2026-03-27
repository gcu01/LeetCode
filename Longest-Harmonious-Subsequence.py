1class Solution(object):
2    def findLHS(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        frequency_map = Counter(nums)
8        max_length = 0
9
10        for num in frequency_map:
11            if num + 1 in frequency_map:
12                current_length = frequency_map[num] + frequency_map[num + 1]
13                max_length = max(max_length, current_length)
14
15        return max_length
16
17
18        nd = dict()
19        for val in nums:
20            nd[val] = nd.get(val, 0) + 1
21        #print("nd = ", nd)
22        mx = 0
23        for key, value in nd.items():            
24            if key+1 in nd.keys():
25                mx = max(mx, nd[key] + nd[key+1])
26        return mx
27
28        ''' takes too much time
29        mx = 0
30        check = []
31        for val in nums:
32            if val-1 in nums and val not in check:
33                mx = max(mx, nd.get(val-1, 0) + nd.get(val, 0))
34                check.append(val)
35            if val+1 in nums and val not in check:
36                mx = max(mx, nd.get(val-1, 0) + nd.get(val, 0))
37                check.append(val)
38        return mx
39        '''
40
41        '''                
42            if nd.get(val-1, 0) == 0:
43                break
44            else:
45                tmp = nd.get(val-1, 0) + nd.get(val, 0)
46                mx = max(mx, tmp)
47            if nd.get(val+1, 0) == 0:
48                break
49            else:
50                tmp = nd.get(val, 0) + nd.get(val+1, 0)
51                mx = max(mx, tmp)            
52        return mx
53        '''
54