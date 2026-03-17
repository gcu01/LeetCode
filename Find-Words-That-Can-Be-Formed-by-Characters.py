1class Solution(object):
2    def countCharacters(self, words, chars):
3        """
4        :type words: List[str]
5        :type chars: str
6        :rtype: int
7        """
8        # revised solution
9        out = 0
10        for word in words:
11            flag = True
12            #print(word)
13            for c in word:
14                if word.count(c) > chars.count(c):
15                    flag = False     
16                    break           
17            if flag:
18                out += len(word)
19                        
20        return out
21
22        # too complicate
23        d_chars = dict()
24        for ch in chars:
25            d_chars[ch] = d_chars.get(ch, 0) + 1
26        #print(d_chars)
27        #res = []
28        out = 0
29        for word in words:
30            flag = True
31            bck = copy.deepcopy(d_chars)
32            #print(word)
33            #print(bck)
34            for c in word:
35                if bck.get(c, 0) != 0:
36                    bck[c] -= 1
37                    #print(bck)
38                else:
39                    flag = False
40                    #print("cont")
41                    continue
42            if flag:
43                out += len(word)
44                #res.append(word)
45        #print(res)
46        return out