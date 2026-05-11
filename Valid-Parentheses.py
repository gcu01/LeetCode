1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        #if len(s) < 2:
8        #    return False
9        pre = ["(", "[", "{"]
10        post = [")", "]", "}"]
11        out = []
12        for i, val in enumerate(s):
13            #print("i=", i, "  val=", val)
14            if val in pre:
15                out.append(val)
16                #print(" pre out=", out)
17            elif len(out) and pre.index(out[-1]) == post.index(val):
18                #print("here")
19                out.pop()
20                #print("post out = ", out)
21            else:
22                return False
23        #print("final out=", out)
24        if len(out):
25            #print("mai mare")
26            return False
27        return True
28