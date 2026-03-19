1class Solution(object):
2    def reverseByType(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        s_lst = list(s)
8        ic, jc = 0, (len(s_lst)-1)        
9        isp, jsp = 0, (len(s_lst)-1)
10        while ic<jc:
11            #print("ic=", ic, "   jc=", jc)
12            #print("s_lst[ic]=", s_lst[ic], "      s_lst[jc]=", s_lst[jc])
13            if s_lst[ic].isalpha() == False:
14                ic += 1
15                continue
16            if s_lst[jc].isalpha() == False:
17                jc -= 1
18                continue
19            s_lst[ic], s_lst[jc] = s_lst[jc], s_lst[ic]
20            ic += 1
21            jc -= 1
22
23        while isp<jsp:
24            if s_lst[isp].isalpha():
25                isp += 1
26                continue
27            if s_lst[jsp].isalpha():
28                jsp -= 1
29                continue
30            s_lst[isp], s_lst[jsp] = s_lst[jsp], s_lst[isp]
31            isp += 1
32            jsp -= 1
33        return "".join(s_lst)