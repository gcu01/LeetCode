1class Solution(object):
2    def mostCommonWord(self, paragraph, banned):
3        """
4        :type paragraph: str
5        :type banned: List[str]
6        :rtype: str
7        """
8        paragraph = paragraph.lower()
9        banned = set(banned)
10        d = dict()
11        for ch in ":;?!'.,":
12            paragraph = paragraph.replace(ch, " ")
13        paragraph = paragraph.split()
14        #print(paragraph)
15        for word in paragraph:
16            d[word] = d.get(word, 0) + 1
17        lst = sorted(d.items(), key = lambda item:item[1], reverse = True)
18        #print(lst)
19        for key, value in lst:
20            if key not in banned:
21                return key
22
23
24
25
26
27
28
29        '''
30        if paragraph[-1] in ".!?,:;":
31            paragraph = paragraph[:len(paragraph)-1]
32        #print(paragraph)
33        for val in ".!?,:;":            
34            paragraph = paragraph.replace(val, " ")
35        paragraph = paragraph.replace("  ", " ")
36        #print(paragraph)
37        word_lst = paragraph.split(" ")
38        #print(word_lst)
39        word_dict = dict()
40        for word in word_lst:
41            word = word.lower()
42            word_dict[word] = word_dict.get(word, 0) + 1
43        #print(word_dict.items())
44        word_lst_sort = sorted(word_dict.items(), key = lambda item:item[1], reverse = True)
45        #print(word_lst_sort)
46        for key, value in word_lst_sort:
47            if key not in banned:
48                return key
49        '''
50
51
52
53
54
55        '''
56        rem = ""
57        for val in paragraph:
58            if val.isalpha() or val == " " or val == ".":
59                rem += val.lower()
60        #rem = rem.split(" ")
61        rem = re.split(r"[ .]", rem)
62        #print(rem)
63        d = dict()
64        for val in rem:
65            if val in d:
66                d[val] += 1
67            else:
68                d[val] = 1
69        d1 = (sorted(d.items(), key=lambda item: item[1], reverse = True))
70        print("d1=", d1)
71        if banned == []:
72            return d1[0][0]
73        for i in range(len(d1)):
74            print("val-", d1[i][0])
75            if d1[i][0] not in banned:
76                return d1[i][0]
77        
78        #if d1[0][0] == banned[0]:
79        #    return d1[1][0]
80        #return d1[0][0]
81        '''