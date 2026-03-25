1class Solution(object):
2    def compress(self, chars):
3        """
4        :type chars: List[str]
5        :rtype: int
6        """
7        s = ""
8        if len(chars) == 1:
9            return 1
10        ch = chars[0]
11        idx = 1
12        for i in range(1, len(chars)):
13            if chars[i] == chars[i-1]:
14                idx += 1
15            elif idx == 1 :
16                s += ch
17                ch = chars[i]
18                idx = 1
19            else:
20                s += ch + str(idx)            
21                ch = chars[i]
22                idx = 1
23        #print("ch=", ch, "   idx=", idx)
24        s += ch +str(idx) if idx>1 else ch
25        #print("s=", s)
26        for i in range(len(s)):
27            chars[i] = s[i]
28        return len(s)