1class Solution(object):
2    def wordPattern(self, pattern, s):
3        """
4        :type pattern: str
5        :type s: str
6        :rtype: bool
7        """
8        words = s.split(" ")
9        if len(pattern) != len(words):
10            return False
11        char_2_word = dict()
12        word_2_char = dict()
13
14        for i in range(len(pattern)):
15            char = pattern[i]
16            word = words[i]
17
18            if char in char_2_word:
19                if char_2_word[char] != word:
20                    return False
21            else:
22                if word in word_2_char:
23                    if word_2_char[word] != char:
24                        return False
25                char_2_word[char] = word
26                word_2_char[word] = char
27        return True    
28
29
30        '''
31        p_d = dict()
32        for val in pattern:
33            if val in p_d.keys():
34                p_d[val] += 1
35            else:
36                p_d[val] = 1
37        p_lst = sorted(p_d.items(), key=lambda item: item[1], reverse = True)
38        print(p_lst)
39        s_d = dict()
40        for val in s.split(" "):
41            if val in s_d.keys():
42                s_d[val] += 1
43            else:
44                s_d[val] = 1
45        s_lst = sorted(s_d.items(), key=lambda item: item[1], reverse = True)
46        print(s_lst)
47        for i in range(len(p_lst)):
48            if p_lst[i][1] != s_lst[i][1]:
49                return False
50        return True      
51
52
53        
54        set_p = set(pattern)
55        print("set_p=", set_p)
56        set_s = set(s.split(" "))
57        print("set_s=", set_s)
58        return True if len(set_p)==len(set_s) else False
59        '''