1class Solution(object):
2    def maxLengthBetweenEqualCharacters(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7
8        first_idx = dict()
9        max_length = -1
10        for i in range(len(s)):
11            if s[i] in first_idx:
12                max_length = max(max_length, i-first_idx[s[i]]-1)
13            else:
14                first_idx[s[i]] = i
15                #print(first_idx)
16        return max_length
17
18
19        '''
20        s_lst = list(s)
21        checked = []
22        max_length = -1
23        for i in range(len(s_lst)):
24            if s.count(s_lst[i]) > 1 and s_lst[i] not in checked:
25                print("s[",i,"]=", s[i])
26                checked.append(s[i])
27                print("checked=", checked)
28                idx2 = s_lst[i+1:].index(s_lst[i])+i
29                print("idx2=", idx2, "  (idx2-i)=", (idx2-i))
30                if max_length < (idx2-i):
31                    max_length = idx2-i
32                    print("new max_length = ", max_length)
33        return max_length
34        '''